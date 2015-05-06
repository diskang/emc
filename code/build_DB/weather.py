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
recordtime 	年月日时分				201408151450
location 	站点名称				交大
temperature 气温					25.5
rain		降水					0
windorient	瞬时风向				130
windspeed 	瞬时风速				0.8
			瞬时能见度
			相对湿度
			瞬时气压
maxtemph 	一小时最高气温			25.7
mintemph 	一小时最低气温			25.5
maxspeedph 	一小时最大风速			2.2
maxspdornt 	一小时最大风速时风向	38
'''
def map_weather_to_db(line):
	ll = line.split("\t")
	if len(ll) != 13:
		raise Exception("invalid line")
	ll = [i.strip() for i in ll]
	t=ll[0]
	t=t[:4]+'-'+t[4:6]+'-'+t[6:8]+' '+t[8:10]+':'+t[10:]
	return "insert into weather values('%s','%s',%s,%s,%s,%s,%s,%s,%s,%s);"%(t,ll[1],ll[2],ll[3],ll[4],ll[5],ll[9],ll[10],ll[11],ll[12])

# conn = pymssql.connect("")	
with open("D:\work\EMC\EMC\weather\shanghaiqixiang_jiaoda.txt") as f:
	line = f.readline()# first line skip
	count =0
	s=set()
	while line:
		line = f.readline()
		if not line.strip():
			break
		count +=1
		exec_string = map_weather_to_db(line)
		if '/' in exec_string:
			continue
		
		cursor.execute(exec_string)
	conn.commit()
	print "count:"+str(count)
conn.close()