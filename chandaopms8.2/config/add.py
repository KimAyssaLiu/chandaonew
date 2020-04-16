import os
import requests

headers = {"Cache-Control": "max-age=0", "Origin": "http://web", "Upgrade-Insecure-Requests": "1",
           "Content-Type": "application/x-www-form-urlencoded",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           "Referer": "http://web/zentao/user-batchCreate-0.html", "Accept-Encoding": "gzip, deflate",
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




def adddept():

    url = "http://web:80/zentao/dept-manageChild.html"
    cookies = {"lang": "zh-cn", "theme": "default", "preProductID": "1", "preBranch": "0", "storyModule": "0", "lastProduct": "1", "productStoryOrder": "id_desc", "windowHeight": "674", "windowWidth": "1519", "sid": "e52t2obj21ll5trk6gt16lgna3"}

    data = {"depts[0]": "项目管理部",
              "depts[1]": "工程部",
              "depts[2]": "网络管理中心",
              "depts[3]": "信息安全部", "maxOrder": "0", "parentDeptID": "0"}
    r = requests.post(url, headers=headers, cookies=cookies, data=data)

def changename():

    data = {"account": "admin", "password": "e10adc3949ba59abbe56e057f20f883e", "referer": "http://web/zentao/my/"}
    url = "http://web:80/zentao/company-edit.html?onlybody=yes"
    cookies = {"lang": "zh-cn", "theme": "default", "windowWidth": "564", "windowHeight": "430", "sid": "e52t2obj21ll5trk6gt16lgna3"}

    data = {"name": "中国移动", "phone": '10086', "fax": '', "address": 'China,Beijing', "zipcode": '330011', "website": "http://", "backyard": "http://", "guest": "0"}
    r = requests.post(url, headers=headers, cookies=cookies, data=data)


def adduser():

    url = "http://web:80/zentao/user-batchCreate-0.html"
    cookies = {"theme": "default", "preProductID": "1", "preBranch": "0", "storyModule": "0", "lastProduct": "1", "productStoryOrder": "id_desc", "qaBugOrder": "id_desc", "lang": "zh-cn", "keepLogin": "on", "za": "admin", "zp": "216c8c31794854639b890f124b767d9adc2df86f", "windowHeight": "722", "windowWidth": "1519", "sid": "e52t2obj21ll5trk6gt16lgna3"}

    data = {"dept[0]": "1", "account[0]": "man1", "realname[0]": "man1", "role[0]": "top", "group[0]": "9", "email[0]": "13045258910@163.com", "gender[0]": "f", "password[0]": "654321", "commiter[0]": '', "join[0]": '', "skype[0]": '', "qq[0]": '', "yahoo[0]": '', "gtalk[0]": '', "wangwang[0]": '', "mobile[0]": '', "phone[0]": '', "address[0]": '', "zipcode[0]": '',
              "dept[1]": "1", "account[1]": "man2", "realname[1]": "man2", "role[1]": "pd", "group[1]": "7", "email[1]": "130665678911@gmail.com", "gender[1]": "f", "password[1]": "111111", "commiter[1]": '', "join[1]": '', "skype[1]": '', "qq[1]": '', "yahoo[1]": '', "gtalk[1]": '', "wangwang[1]": '', "mobile[1]": '', "phone[1]": '', "address[1]": '', "zipcode[1]": '',
              "dept[2]": "2", "account[2]": "worker1", "realname[2]": "worker1", "role[2]": "td", "group[2]": "6", "email[2]": "13047778912@yahoo.com", "gender[2]": "f", "password[2]": "222222", "commiter[2]": '', "join[2]": '', "skype[2]": '', "qq[2]": '', "yahoo[2]": '', "gtalk[2]": '', "wangwang[2]": '', "mobile[2]": '', "phone[2]": '', "address[2]": '', "zipcode[2]": '',
              "dept[3]": "2", "account[3]": "worker2", "realname[3]": "worker2", "role[3]": "dev", "group[3]": "2", "email[3]": "123456@gmail.com", "gender[3]": "m", "password[3]": "333333", "commiter[3]": '', "join[3]": '', "skype[3]": '', "qq[3]": '', "yahoo[3]": '', "gtalk[3]": '', "wangwang[3]": '', "mobile[3]": '', "phone[3]": '', "address[3]": '', "zipcode[3]": '',
              "dept[4]": "2", "account[4]": "worker3", "realname[4]": "worker3", "role[4]": "dev", "group[4]": "2", "email[4]": "13045678972@126.com", "gender[4]": "m", "password[4]": "444444", "commiter[4]": '', "join[4]": '', "skype[4]": '', "qq[4]": '', "yahoo[4]": '', "gtalk[4]": '', "wangwang[4]": '', "mobile[4]": '', "phone[4]": '', "address[4]": '', "zipcode[4]": '',
              "dept[5]": "2", "account[5]": "worker4", "realname[5]": "worker4", "role[5]": "qa", "group[5]": "3", "email[5]": "13345678972@126.com", "gender[5]": "m", "password[5]": "555555", "commiter[5]": '', "join[5]": '', "skype[5]": '', "qq[5]": '', "yahoo[5]": '', "gtalk[5]": '', "wangwang[5]": '', "mobile[5]": '', "phone[5]": '', "address[5]": '', "zipcode[5]": '',
              "dept[6]": "3", "account[6]": "neter1", "realname[6]": "neter1", "role[6]": "qd", "group[6]": "8", "email[6]": "neter1@126.com", "gender[6]": "m", "password[6]": "666666", "commiter[6]": '', "join[6]": '', "skype[6]": '', "qq[6]": '', "yahoo[6]": '', "gtalk[6]": '', "wangwang[6]": '', "mobile[6]": '', "phone[6]": '', "address[6]": '', "zipcode[6]": '',
              "dept[7]": "3", "account[7]": "neter2", "realname[7]": "neter2", "role[7]": "qa", "group[7]": "3", "email[7]": "neter2@126.com", "gender[7]": "m", "password[7]": "777777", "commiter[7]": '', "join[7]": '', "skype[7]": '', "qq[7]": '', "yahoo[7]": '', "gtalk[7]": '', "wangwang[7]": '', "mobile[7]": '', "phone[7]": '', "address[7]": '', "zipcode[7]": '',
              "dept[8]": "4", "account[8]": "secer1", "realname[8]": "secer1", "role[8]": "qa", "group[8]": "3", "email[8]": "secer1@126.com", "gender[8]": "m", "password[8]": "888888", "commiter[8]": '', "join[8]": '', "skype[8]": '', "qq[8]": '', "yahoo[8]": '', "gtalk[8]": '', "wangwang[8]": '', "mobile[8]": '', "phone[8]": '', "address[8]": '', "zipcode[8]": '',
              "dept[9]": "4", "account[9]": "secer2", "realname[9]": "secer2", "role[9]": "qa", "group[9]": "3", "email[9]": "secer2@126.com", "gender[9]": "m", "password[9]": "999999", "commiter[9]": '', "join[9]": '', "skype[9]": '', "qq[9]": '', "yahoo[9]": '', "gtalk[9]": '', "wangwang[9]": '', "mobile[9]": '', "phone[9]": '', "address[9]": '', "zipcode[9]": '',
              "verifyPassword": "123456"}

    r = requests.post(url, headers=headers, cookies=cookies, data=data)

    print(r.status_code)
    if (r.status_code == 200):
       print("Config success")
    else:
       print("Config fail")


if __name__ == '__main__':
    login1()
    login2()
    adddept()
    changename()
    adduser()
