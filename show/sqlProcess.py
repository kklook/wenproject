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
        self.cursor.execute('create table classbase (className char(40) not NULL ,classId char(12) NOT NULL ,classOrder char(5) NOT NULL,classPoint float NOT NULL,classTeacher char(20) NOT NULL,PRIMARY KEY (classId,classOrder))ENGINE= MYISAM CHARACTER SET utf8 ')
        self.cursor.execute('create table classtime (classId char(12) NOT NULL,classOrder char(5) NOT NULL ,classLong char(5) ,classFre char(4),classWeek int ,classTime char(5),clasStep int,FOREIGN KEY(classId,classOrder) REFERENCES classbase(classId,classOrder)) ENGINE= MYISAM CHARACTER SET utf8 ')
        self.cursor.execute('create table classwhere (classId char(12) NOT NULL ,classOrder char(5) NOT NULL ,classPlace char(50),clasStep int,FOREIGN KEY(classId,classOrder) REFERENCES classbase(classId,classOrder)) ENGINE= MYISAM CHARACTER SET utf8 ')
    def sqlInsert(self,base,time,where):
        self.cursor.execute('insert into classbase(className,classId,classOrder,classPoint,classTeacher) values("%s","%s","%s",%s,"%s")' %(base['className'],base['classId'],base['classOrder'],base['classPoint'],base['classTeacher']))
        weekvalue={'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'日':7}
        pattern=re.compile(r'^(.*)周\(?(单|双)?\)? 星期(一|二|三|四|五|六|日) (.*)节$')
        if isinstance(time,list):
            i=0
            for t in time:
                i=i+1
                pattern=re.compile(r'^(.*)周\(?(单|双)?\)? 星期(一|二|三|四|五|六|日) (.*)节$')
                #print t+"ok"
                result=re.search(pattern,t)
                if result!=None:
                    long=result.group(1)
                    if(result.group(2)==None):
                        fre='/s'
                    else:
                        fre=result.group(2)
                    week=weekvalue[result.group(3)]
                    classtime=result.group(4)
                    self.cursor.execute('insert into classtime VALUES ("%s","%s","%s","%s",%s,"%s",%s)'%(base['classId'],base['classOrder'],long,fre,week,classtime,i))
                else:
                    pattern=re.compile(r'(.*)周\(?(单|双)?\)?')
                    result=re.search(pattern,t)
                    if(result.group(2)==None):
                        fre='/s'
                    else:
                        fre=result.group(2)
                    long=result.group(1)
                    self.cursor.execute('insert into classtime(classId,classOrder,classLong,classFre,classStep) VALUE ("%s","%s","%s","%s",%s)'%(base['classId'],base['classOrder'],long,fre,i))
        elif time=='/s':
            self.cursor.execute('insert into classtime(classId,classOrder,classStep) VALUES ("%s","%s",%s)'%(base['classId'],base['classOrder'],1))
        else:
            result=re.search(pattern,time)
            long=result.group(1)
            if(result.group(2)==None):
                fre='/s'
            else:
                fre=result.group(2)
            week=weekvalue[result.group(3)]
            classtime=result.group(4)
            self.cursor.execute('insert into classtime(classId,classOrder,classLong,classFre,classWeek,classTime,classStep) VALUES("%s","%s","%s","%s",%s,"%s",%s)'%(base['classId'],base['classOrder'],long,fre,week,classtime,1))
        if isinstance(where,list):
            i=0
            for w in where:
                i=i+1
                self.cursor.execute('insert into classwhere VALUES ("%s","%s","%s",%s)'%(base['classId'],base['classOrder'],w,i))
        elif where=='/s':
            self.cursor.execute('insert into classwhere(classId,classOrder,classStep) VALUES ("%s","%s",%s)'%(base['classId'],base['classOrder'],0))
        else:
            self.cursor.execute('insert into classwhere(classId,classOrder,classPlace,classStep) VALUES ("%s","%s","%s",%s)'%(base['classId'],base['classOrder'],where,0))
    def getLock(self):
        self.cursor.execute("select get_lock(%s,%s)"%('"lock"',5))
        ret=self.cursor.fetchone()
        print ret
        if ret[0]==1:
            return True
        else:
            return False
    def releaseLock(self):
        self.cursor.execute('select release_lock(%s)'%('"lock"'))
        ret=self.cursor.fetchone()
        print ret
        if ret[0]==1:
            return True
        else:
            return False
    def defaultChange(self):
        self.cursor.execute('create table change (classId char(12) NOT NULL ,classOrder char(5) NOT NULL,classStep int)')





link=MySqlLink()