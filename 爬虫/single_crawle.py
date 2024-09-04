"""
example04.py - 单线程版本爬虫
"""
import os
import re

import requests

def download_picture(url):
    filename = url[url.rfind('/') + 1:]
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(f'images/beauty/{filename}', 'wb') as file:
            file.write(resp.content)


def main():
    if not os.path.exists('images/beauty'):
        os.makedirs('images/beauty')
    resp = requests.get(
        url='https://www.58pic.com/tupian/gongzhonghaofengmian-815-0-default-0-5-%E5%85%AC%E4%BC%97%E5%8F%B7%E5%B0%81%E9%9D%A2-0_2_276_0_0_1233_0-0-0-0-0-0-0-0-0-0-0-0-0-0-2.html',
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
        )
    src = re.compile(r'(//[^\'" >]+webp)').findall(resp.text)
    for v in src:
        print(v)
        download_picture(f'https:{v}')

if __name__ == '__main__':
    main()