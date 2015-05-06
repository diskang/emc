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
fromaccount	学生卡号（匿名化）	B62997
toaccount	商户代码			1000029
syscode		商户所属系统代码          	34
timestamp	交易时间          	2014-10-01 09:50:36
amount		交易金额（单位分）	150
'''

def map_trade_to_db(line):
	ll = line.split("\t")
	if len(ll) != 5:
		raise Exception("invalid line")
	ll = [i.strip() for i in ll]
	return "insert into trade values('%s','%s',%s,'%s',%s);"%(ll[0],ll[1],ll[2],ll[3],ll[4])

# conn = pymssql.connect("")	
with open("../../data/trade.txt") as f:
	line = f.readline()# first line skip
	count =0
	while line:
		line = f.readline()
		if not line.strip():
			break
		count +=1
		exec_string = map_trade_to_db(line)
		#print exec_string
		cursor.execute(exec_string)
	conn.commit()
	print "count:"+str(count)
conn.close()