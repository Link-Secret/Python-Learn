#@Time  :   2018/6/11 18:25
#@Author:   zjl
#@File  :   csdn.py

import requests
from requests import RequestException

def get_page_index(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    try:
        response = requests.get(url,headers = header)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('访问出错')
        return None

def main():
    html = get_page_index('https://blog.csdn.net/sentimental_dog/article/details/52661974')
    print(html)


if __name__ == '__main__':
    for i in range(100):
        main()