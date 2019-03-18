#!/usr/bin/env python3
# _*_ coding=utf-8 _*_

import os
import requests
import re
import sys
from Crypto.Cipher import AES
from multiprocessing import Pool

def download(url):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50'}
    return requests.get(url, headers = headers)

def get(text, pattern):
    obj = re.search(pattern, text, re.M)
    return obj.group(1)

def find(text, pattern):
    return re.search(pattern, text, re.M) is not None

def parse(text, pattern):
    for iter in re.finditer(pattern, text, re.M):
        yield iter.group()[1:]

def remove_list(m3u8_list):
    for m3u8 in m3u8_list:
        os.remove(m3u8)

class VideoDownload:
    def __init__(self, url, key):
        self.key = key
        self.m3u8_list = []
        self.url = url

    def write(self, url, file):
        cryptor = AES.new(self.key, AES.MODE_CBC, self.key)
        with open(file, 'wb') as f:
            f.write(cryptor.decrypt(download(url).content))

    def start(self, text, pattern):
        p = Pool(4)
        for m3u8 in parse(text, pattern):
            self.m3u8_list.append(m3u8)
            #print('url: ', os.path.join(self.url, m3u8))
            p.apply_async(self.write, args=(os.path.join(self.url, m3u8), m3u8))
        p.close()
        p.join()

    def get_list(self):
        return self.m3u8_list

    def __transfer(self, from_file, to_file):
        os.system('ffmpeg -i "concat:{}" -c copy \"{}\"'.format(from_file, to_file))

    def transfer(self, file):
        self.m3u8_list.sort()
        length = len(self.m3u8_list) 
        maxfile = 200  # 最大文件打开个数 ulimit -n 2000
        outfiles = []
        for i in range(0, length, maxfile):
            to_file = '{}.mp4'.format(i)
            outfiles.append(to_file)
            self.__transfer('|'.join(self.m3u8_list[i:i+maxfile]), to_file)
        self.__transfer('|'.join(outfiles), file)

        remove_list(outfiles)
        remove_list(self.m3u8_list)

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        raise BaseException('input error')

    text = download(sys.argv[1]).text.encode('latin1').decode('utf-8')
    # 获取m3u8的地址
    url = get(text, r"video: '(.*)'")
    # 获取视频的名称
    filename = get(text, r'<title>(.*)</title>')
    #print('url: {}\nfile: {}'.format(url, filename))

    while True:
        text = download(url).text
        if not text.startswith('#EXTM3U'):
            raise BaseException('m3u8 error url')

        if find(text, r'#EXT-X-STREAM-INF'):
            url = os.path.join(url.rsplit('/', 1)[0], get(text, r'(.*).m3u8') + '.m3u8')
        else:
            break

    # 加密类型
    encry = get(text, r'#EXT-X-KEY:METHOD=(.*),URI=".*"')
    # key
    key = get(text, r'#EXT-X-KEY:METHOD=.*,URI="(.*)"')
    #print('encry: {}, key: {}'.format(encry, key))
    # 密钥
    key_data = download(os.path.join(url.rsplit('/', 1)[0], key)).content
    #print('key data: ', key_data)
    video_download = VideoDownload(url.rsplit('/', 1)[0], key_data)
    print('download begin')
    video_download.start(text, r'$\n[A-Za-z0-9]+.ts')
    print('download end')
    video_download.transfer(filename + '.mp4')
    print('transfer end')