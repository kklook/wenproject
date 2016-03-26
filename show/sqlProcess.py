#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import mysql.connector
class MySqlLink(object):
    def __init__(self):
        self.myUser='root'
        self.myPass='liang123'
        self.myDatabaseName='test'
    def defaultSet(self):
        connect=mysql.connector.connect(user=self.myUser,password=self.myPass,database=self.myDatabaseName,use_unicode=True)
        self.cursor=connect.cursor()
        self.cursor.execute('create table classbase (className char(20) not NULL ,classId char(12) primary key NOT NULL ,classOrder char(2) NOT NULL,classPoint float NOT NULL,classTeacher char(10) NOT NULL)')
        self.cursor.execute('create table classtime (classId char(12) primary key NOT NULL ,classLong1 char(5) NOT NULL ,classWeek1 int NOT NULL ,classTime1 char(5) NOT NULL,classLong2 char(5) ,classWeek2 int ,classTime2 char(5),FOREIGN KEY(classId) REFERENCES classbase(classId))')
        self.cursor.execute('create table classwhere (classId char(12) PRIMARY KEY NOT NULL ,classPlace1 char(50) NOT NULL,classPlace2 char(50),FOREIGN KEY(classId) REFERENCES classbase(classId))')
link=MySqlLink()
link.defaultSet()

