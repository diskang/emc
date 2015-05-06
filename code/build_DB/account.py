#!/usr/bin/env python
# coding: utf-8
import pymssql

HOST="202.120.38.227"
DB_USER = "icare-PC\icare"
DB_PW = "qwert"
DB_NAME="EMC"
conn= pymssql.connect(HOST,DB_USER,DB_PW,DB_NAME)
cursor = conn.cursor()
'''
account      学生卡号（匿名化）   A16100
studentcode  学生学号（匿名化）   76118305
gender       性别                 男
yearofbirth  出生年               1989
grade        入学年               2012
type         类型（本科/硕士/博士）硕士
'''
HASH = {"男":"1","女":"0","本科":"f","硕士":"b","博士":"a"}
def map_account_to_db(line):
	ll = line.split("\t")
	if len(ll) != 6:
		raise Exception("invalid line")
	ll = [i.strip() for i in ll]
	# _account,_studentcode,_gender,_yearofbirth,_grade,_type = ll[0],ll[1],ll[2],ll[3],ll[4],ll[5]
	ll[2] = HASH.get(ll[2])
	ll[5] = HASH.get(ll[5])
	return "insert into account values('%s','%s','%s','%s','%s','%s');"%(ll[0],ll[1],ll[2],ll[3],ll[4],ll[5])

# conn = pymssql.connect("")	
with open("../../data/account.txt") as f:
	line = f.readline()# first line skip
	count =0
	while line:
		line = f.readline()
		if not line.strip():
			break
		count +=1
		exec_string = map_account_to_db(line)
		cursor.execute(exec_string)
	conn.commit()
	print "count:"+str(count)
conn.close()