import os
import requests

headers = {"Cache-Control": "max-age=0",
               "Origin": "http://web", "Upgrade-Insecure-Requests": "1",
               "Content-Type": "application/x-www-form-urlencoded",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
               "Referer": "http://web/zentao/product-create.html", "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8", "Connection": "close"}


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

def addproduct():

    url = "http://web:80/zentao/product-create.html"
    cookies = {"lang": "zh-cn", "theme": "default", "windowHeight": "722", "windowWidth": "1536",

               "sid": "e52t2obj21ll5trk6gt16lgna3"}

    data = {"name": "咪咕视频", "code": "001", "PO": "admin", "QD": "man1", "RD": "man2", "type": "normal",

            "desc": "中国移动旗下视频播放软件", "acl": "custom", "whitelist[]": "1", "whitelist[]": "2", "whitelist[]": "6",

            "whitelist[]": "7", "whitelist[]": "8", "whitelist[]": "9"}

    r = requests.post(url, headers=headers, cookies=cookies, data=data)

    print(r.content)

def addbug():


    url = "http://web:80/zentao/bug-create-1-0-moduleID=0.html"
    cookies = {"lang": "zh-cn", "theme": "default", "lastProduct": "1", "preProductID": "1", "preBranch": "0", "storyModule": "0", "productStoryOrder": "id_desc", "lastProject": "1", "preProjectID": "1", "moduleBrowseParam": "0", "productBrowseParam": "0", "projectTaskOrder": "status%2Cid_desc", "qaBugOrder": "id_desc", "projectStoryOrder": "pri", "windowHeight": "722", "windowWidth": "1519", "sid": "e52t2obj21ll5trk6gt16lgna3"}
    headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryyBAlWobdLJ4epTHZ", "Origin": "http://web", "Referer": "http://web/zentao/bug-create-1-0-moduleID=0.html", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8", "Connection": "close"}
    data = "------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"product\"\r\n\r\n1\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"module\"\r\n\r\n0\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"project\"\r\n\r\n\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"openedBuild[]\"\r\n\r\ntrunk\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"assignedTo\"\r\n\r\nman1\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\ncodeerror\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"os\"\r\n\r\n\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"browser\"\r\n\r\n\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"color\"\r\n\r\n\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n咪咕视频存在代码执行漏洞\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"severity\"\r\n\r\n3\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"pri\"\r\n\r\n0\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"steps\"\r\n\r\n<p><br />\n</p>\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"story\"\r\n\r\n0\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"task\"\r\n\r\n0\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"mailto[]\"\r\n\r\n\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"mailto[]\"\r\n\r\nman1\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"mailto[]\"\r\n\r\nman2\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"keywords\"\r\n\r\n\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"files[]\"\r\n\r\n\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"labels[]\"\r\n\r\n\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"case\"\r\n\r\n0\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"caseVersion\"\r\n\r\n0\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"result\"\r\n\r\n0\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ\r\nContent-Disposition: form-data; name=\"testtask\"\r\n\r\n0\r\n------WebKitFormBoundaryyBAlWobdLJ4epTHZ--\r\n"

    r = requests.post(url, headers=headers, cookies=cookies, data=data.encode("utf-8").decode("latin1"))

    print(r.content)
    print(r.status_code)
    if (r.status_code == 200):
       print("Config success")
    else:
       print("Config fail")

if __name__ == '__main__':

    login1()
    login2()
    addproduct() 
    addbug()




