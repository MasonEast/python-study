from threading import Thread

import requests

class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('Users/Hao/' + filename, 'wb') as f:
            f.write(resp.content)

def main():
    resp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
    data_model = resp.json()
    print(data_model)
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHandler(url).start()

if __name__ == '__main__':
    main()