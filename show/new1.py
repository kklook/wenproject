#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import urllib2
import urllib
import cookielib
import webbrowser
from bs4 import BeautifulSoup
import sys,os
#获取脚本文件的当前路径
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
class myCookie(object):
    def __init__(self,id,ps):
        self.cookie=cookielib.MozillaCookieJar()
        self.handle=urllib2.HTTPCookieProcessor(self.cookie)
        self.opener=urllib2.build_opener(self.handle)
        self.id=id
        self.ps=ps
        self.value={'Login.Token1':self.id,'Login.Token2':self.ps}
        self.data=urllib.urlencode(self.value)
    def getimg(self):
        webbrowser.open('http://ssfw3.hlju.edu.cn/ssfw/jwcaptcha.do')
    def open(self):
        self.opener.open('http://my.hlju.edu.cn/userPasswordValidate.portal',self.data)
        self.test=self.opener.open('http://ssfw3.hlju.edu.cn/ssfw/j_spring_ids_security_check')
        self.page=self.opener.open('http://ssfw3.hlju.edu.cn/ssfw/pkgl/kcbxx/4/2015-2016-2.do')
        if self.test.read().find('success')!=-1:
            return self.page.read()
        else:
            return -1
    def getclass(self):
        self.open()
        for i in range(1,475,1):
            findValue={'ctx':'/ssfw','qXnxqdm':'2015-2016-2','curPageNo':i}
            findDate=urllib.urlencode(findValue)
            page=self.opener.open('http://ssfw3.hlju.edu.cn/ssfw/pkgl/rwapcx.do',findDate)
            readpage=page.read()
            with open(cur_file_dir()+'\source\\'+str(i)+'.html','w') as f:
                f.write(readpage)
    def select(self):
        with open('text.html','r') as f:
            information=f.read()
        soup=BeautifulSoup(information,'lxml')
        #soup=BeautifulSoup(self.readpage,'lxml')
        print soup.find_all('table')
cookie=myCookie('20122617','liang123')
cookie.getclass()
