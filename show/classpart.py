#/usr/bin/evn python
# -*- coding:utf-8 -*-
class UserClass(object):
    def __init__(self,classId,className,classTime,classPlace,classTeacher):
        self.classId=classId
        self.className=className
        self.classTime=classTime
        self.classPlace=classPlace
        self.classTeacher=classTeacher
    def jsondict(self,user):
        return{
            'classId':user.classId,
            'className':user.className,
            'classTime':user.classTime,
            'classPlace':user.classPlace,
            'classTeacher':user.classTeacher
        }

