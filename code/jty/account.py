# -*- coding: utf-8 -*-
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
db = client.EMC

accountFile = open("account.txt",encoding="utf-8")
accountFile.readline()
for line in accountFile :
	accountArr = line.strip().split('\t')
	account = {}
	account['account'] = accountArr[0]
	account['studentcode'] = int(accountArr[1])
	db.account.save(account)

print ("account finish")
