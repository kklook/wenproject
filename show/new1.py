#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import urllib2
import urllib
import cookielib
import webbrowser
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
        test=self.opener.open('http://ssfw3.hlju.edu.cn/ssfw/j_spring_ids_security_check')
        page=self.opener.open('http://ssfw3.hlju.edu.cn/ssfw/pkgl/kcbxx/4/2015-2016-2.do')
        if test.read().find('success')!=-1:
            with open('userlist.txt','a') as f:
                f.write(self.id+"  "+self.ps+"\n")
            return page.read()
        else:
            return -1
