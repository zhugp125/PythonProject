#!/usr/bin/env python3
# _*_ coding=utf-8 _*_

import os
import requests
import re
import sys
from Crypto.Cipher import AES
from multiprocessing import Pool

def download(url):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    try:
        return requests.get(url, headers=headers, timeout=5)
    except requests.exceptions.Timeout:
        return None

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
            print('download ts: ', url)
            r = download(url)
            if r is not None and r.status_code == 200:
                f.write(cryptor.decrypt(r.content))

    def start(self, text, pattern):
        self.m3u8_list.clear()
        for m3u8 in parse(text, pattern):
            self.m3u8_list.append(m3u8)
        
        p = Pool(4)
        for m3u8 in self.m3u8_list:
            p.apply_async(self.write, args=(os.path.join(self.url, m3u8), m3u8))
        p.close()
        p.join()

    def __transfer(self, from_file, to_file):
        os.system('ffmpeg -i "concat:{}" -c copy \"{}\"'.format(from_file, to_file))

    def transfer(self, file):
        length = len(self.m3u8_list) 
        outfiles = []
        maxfile = 200  # 最大文件打开个数 ulimit -n 2000
        start = 0
        while start < length:
            to_file = '{}.ts'.format(start)
            outfiles.append(to_file)
            self.__transfer('|'.join(self.m3u8_list[start:start+maxfile]), to_file)
            start = start + maxfile
        self.__transfer('|'.join(outfiles), file)

        remove_list(outfiles)
        remove_list(self.m3u8_list)

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        raise BaseException('input error')

    text = download(sys.argv[1]).text.encode('latin1').decode('utf-8')
    # 获取m3u8的地址
    url = get(text, r'([a-zA-z]+://[^\s]*.m3u8)')
    # 获取视频的名称
    filename = get(text, r'<h1 class="h1">(.*)</h1>')
    print('url: {}\nfile: {}'.format(url, filename))

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