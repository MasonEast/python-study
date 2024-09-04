import os 
from concurrent.futures import ThreadPoolExecutor

import requests

path = 'images/beauty'
def download_picture(url):
    filename = url[url.rfind('/') + 1:]
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(f'{path}/{filename}', 'wb') as file:
            file.write(resp.content)

def main():
    if not os.path.exists(path):
        os.makedirs(path)
    with ThreadPoolExecutor(max_workers=16) as pool:
        for page in range(3):
            resp = requests.get(f'https://image.so.com/zjl?ch=beauty&sn={page * 30}')
            if resp.status_code == 200:
                list = resp.json()['list']
                for item in list:
                    pool.submit(download_picture, item)


if __name__ == '__main__':
    main()