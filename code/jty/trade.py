# -*- coding: utf-8 -*-
import pymongo
import time

r1=[1000001,1000002,1000003,1000005,1000006,1000007,1000010,1000011,1000014,1000015,1000202,1000204,1000219]
r2=[1000027,1000029,1000030,1000031,1000037,1000038,1000039,1000040,1000041,1000215]
r3=[1000232,1000231,1000233]
r4=[1000055,1000056,1000057,1000060,1000108,1000132,1000136,1000157,1000159,1000181,1000182,1000183,1000184,1000185,1000186,1000187,1000210,1000211,1000212,1000213,1000216]
r5=[1000061,1000062,1000103]
r6=[1000178,1000179,1000180]

client = pymongo.MongoClient('localhost', 27017)
db = client.EMC

tradeFile = open("trade.txt",encoding="utf-8")
tradeFile.readline()

accountColle = {}
accountFile = open("account.txt",encoding="utf-8")
accountFile.readline()
for line in accountFile :
	accountArr = line.strip().split('\t')
	accountColle.update({accountArr[0]:accountArr[1]})

cnt=0
for line in tradeFile :
	tradeArr = line.strip().split('\t')
	trade = {}
	trade['fromaccount'] = tradeArr[0]
	trade['toaccount'] = int(tradeArr[1])
	trade['syscode'] = int(tradeArr[2])
	trade['timestamp'] = int(time.mktime(time.strptime(tradeArr[3],'%Y-%m-%d %H:%M:%S'))*1000)
	trade['amount'] = int(tradeArr[4])
	trade['studentcode'] = accountColle[tradeArr[0]]
	trade['addr'] = "x"
	if int(tradeArr[1]) in r1 :
		trade['addr'] = "1"
	elif int(tradeArr[1]) in r2:
		trade['addr'] = "2"
	elif int(tradeArr[1]) in r3:
		trade['addr'] = "3"
	elif int(tradeArr[1]) in r4:
		trade['addr'] = "4"
	elif int(tradeArr[1]) in r5:
		trade['addr'] = "5"
	elif int(tradeArr[1]) in r6:
		trade['addr'] = "6"
	# print (trade)
	db.trade.save(trade)
	if (cnt%1000==0):
		print (cnt/7915289*100)
	cnt+=1

print ("trade finish")
