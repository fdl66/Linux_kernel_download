#!/usr/bin/env python
# coding=utf-8

import requests
import threading
import re

#请填写你自己的下载保存路径
DOWNLOAD_DIR="/home/kernel/"

url='https://www.kernel.org/pub/linux/kernel/'
versiontest=[
    "v1.0/",
]
version=[
    "v1.0/",
    "v1.1/",
    "v1.2/",
    "v1.3/",
    "v2.0/",
    "v2.1/",
    "v2.2/",
    "v2.3/",
    "v2.4/",
    "v2.5/",
    "v2.6/",
    "v3.0/",
    "v3.x/",
    "v4.x/",
]
url1=[]
url2=[]
def gener_url1():
    for item in version:
        url_tmp=url+item
        url1.append(url_tmp)

def gener_url2():
    for item in url1:
        page = requests.get(item)
        data = page.text
        page.close
        data = re.findall(r'linux[^>"]*gz', data)
        kernelversion = []
        for jtem in data:
            if jtem not in kernelversion:
                kernelversion.append(jtem)
                url2.append(item+jtem)

def download(file_url):
    r=requests.get(file_url)
    filename=file_url.split("/")[-1]
    with open(DOWNLOAD_DIR+filename,"wb") as code:
        code.write(r.content)


def check_url2():
    for item in url2:
        print item
    print len(url2)

def start_download():
    for item in url2:
        print item
        download(item)


def main():
    gener_url1()
    gener_url2()
    # check_url2()
    start_download()

if __name__=="__main__":
    main()
