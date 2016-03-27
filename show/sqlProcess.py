#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import mysql.connector
import re
class MySqlLink(object):
    def __init__(self):
        self.myUser='root'
        self.myPass='liang123'
        self.myDatabaseName='test'
        self.connect=mysql.connector.connect(user=self.myUser,password=self.myPass,database=self.myDatabaseName,use_unicode=True)
        self.cursor=self.connect.cursor()
    def defaultSet(self):
        self.cursor.execute('create table classbase (className char(20) not NULL ,classId char(12) NOT NULL ,classOrder char(2) NOT NULL,classPoint float NOT NULL,classTeacher char(20) NOT NULL,PRIMARY KEY (classId,classOrder))ENGINE= MYISAM CHARACTER SET utf8 ')
        self.cursor.execute('create table classtime (classId char(12) NOT NULL,classOrder char(2) NOT NULL ,classLong1 char(5) ,classFre1 char(4),classWeek1 int ,classTime1 char(5),classLong2 char(5),classFre2 char(2) ,classWeek2 int ,classTime2 char(5),PRIMARY KEY (classId,classOrder),FOREIGN KEY(classId,classOrder) REFERENCES classbase(classId,classOrder)) ENGINE= MYISAM CHARACTER SET utf8 ')
        self.cursor.execute('create table classwhere (classId char(12) NOT NULL ,classOrder char(2) NOT NULL ,classPlace1 char(50),classPlace2 char(50),PRIMARY KEY (classId,classOrder),FOREIGN KEY(classId,classOrder) REFERENCES classbase(classId,classOrder)) ENGINE= MYISAM CHARACTER SET utf8 ')
    def sqlInsert(self,base,time,where):
        self.cursor.execute('insert into classbase(className,classId,classOrder,classPoint,classTeacher) values("%s","%s","%s",%s,"%s")' %(base['className'],base['classId'],base['classOrder'],base['classPoint'],base['classTeacher']))
        weekvalue={'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'日':7}
        pattern=re.compile(r'(.*)周\(?(单|双)?\)? 星期(一|二|三|四|五|六|日) (.*)节')
        if isinstance(time,list):
            long=[]
            week=[]
            classtime=[]
            fre=[]
            for t in time:
                result=re.search(pattern,t)
                long.append(result.group(1))
                if(result.group(2)==None):
                    fre.append(' ')
                else:
                    fre.append(result.group(2))
                week.append(weekvalue[result.group(3)])
                classtime.append(result.group(4))
            self.cursor.execute('insert into classtime VALUES ("%s","%s","%s","%s",%s,"%s","%s","%s",%s,"%s")'%(base['classId'],base['classOrder'],long[0],fre[0],week[0],classtime[0],long[1],fre[1],week[1],classtime[1]))
        elif time=='/s':
            self.cursor.execute('insert into classtime(classId,classOrder) VALUES ("%s","%s")'%(base['classId'],base['classOrder']))
        else:
            result=re.search(pattern,time)
            long=result.group(1)
            if(result.group(2)==None):
                fre='/s'
            else:
                fre=result.group(2)
            week=weekvalue[result.group(3)]
            classtime=result.group(4)
            self.cursor.execute('insert into classtime(classId,classOrder,classLong1,classFre1,classWeek1,classTime1) VALUES("%s","%s","%s","%s",%s,"%s")'%(base['classId'],base['classOrder'],long,fre,week,classtime))
        if isinstance(where,list):
            self.cursor.execute('insert into classwhere VALUES ("%s","%s","%s","%s")'%(base['classId'],base['classOrder'],where[0],where[1]))
        elif where=='/s':
            self.cursor.execute('insert into classwhere(classId,classOrder) VALUES ("%s","%s")'%(base['classId'],base['classOrder']))
        else:
            self.cursor.execute('insert into classwhere(classId,classOrder,classPlace1) VALUES ("%s","%s","%s")'%(base['classId'],base['classOrder'],where))




link=MySqlLink()

