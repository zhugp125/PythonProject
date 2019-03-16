#!/usr/bin/env python3
# _*_ coding=utf-8 _*_

import os
import requests
import re
import sys
from Crypto.Cipher import AES

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

def write_url(url, cryptor, f):
    f.write(cryptor.decrypt(download(url).content))

def transfer(from_file, to_file):
    os.system('ffmpeg -y -i \"{}\" -c:v libx264 -c:a copy -bsf:a aac_adtstoasc \"{}\"'.format(from_file, to_file))

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
        #print('url_____________', url)
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
    url_pre = url.rsplit('/', 1)[0]
    #print('url............. ', url_pre)
    key_data = download(os.path.join(url_pre, key)).content
    #print('key data: ', key_data)
    cryptor = AES.new(key_data, AES.MODE_CBC, key_data)
    
    from_file = filename + '.ts'
    with open(from_file, 'wb') as f:
        for m3u8 in parse(text, r'$\n[A-Za-z0-9]+.ts'):
            m3u8_url = os.path.join(url_pre, m3u8)
            print('url: ', m3u8_url)
            write_url(m3u8_url, cryptor, f)

    to_file = filename + '.mp4'
    transfer(from_file, to_file)