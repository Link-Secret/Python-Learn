#@Time  :   2018/6/10 10:45
#@Author:   zjl
#@File  :   Test.py

import requests
from requests import RequestException

def get_page_detail(url):
    header = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    try:
        response = requests.get(url,headers = header)
        if response.status_code == 200:
            print(response.text)
            return response.text
        return None
    except RequestException:
        print("访问详情页出错",url)
        return None

def main():
    get_page_detail('http://toutiao.com/group/6565057165717930504/')

if __name__ == '__main__':
    main()