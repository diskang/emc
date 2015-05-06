#!/usr/bin/env python
# coding: utf-8
import pymssql

HOST="127.0.0.1"
DB_USER = "icare-PC\icare"
DB_PW = "qwert"
DB_NAME="EMC"
conn= pymssql.connect(HOST,DB_USER,DB_PW,DB_NAME)
cursor = conn.cursor()
'''
syscode     商户系统代码      34
codename    商户系统名称      闵行第二食堂
toaccount   商户代码          1000031
accountname 商户名称          川味点心
address     商户地点(有缺失)
opendata    商户成立时间      2007-07-04
'''
def map_merchant_to_db(line):
	ll = line.split("\t")
	if len(ll) != 6:
		raise Exception("invalid line")
	ll = [i.strip() for i in ll]
	return "insert into merchant values(%s,'%s','%s','%s','%s','%s');"%(ll[0],ll[1],ll[2],ll[3],ll[4],ll[5])

# conn = pymssql.connect("")	
with open("../../data/merchant.csv") as f:
	line = f.readline()# first line skip
	count =0
	s=set()
	while line:
		line = f.readline()
		if not line.strip():
			break
		count +=1
		exec_string = map_merchant_to_db(line)
		print exec_string
		# cursor.execute(exec_string)
	# conn.commit()
	print "count:"+str(count)
conn.close()