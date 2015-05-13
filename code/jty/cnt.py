# -*- coding: utf-8 -*-
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
db = client.EMC

tradeFile = open("account.txt",encoding="utf-8")
tradeFile.readline()

cnt=0
for line in tradeFile :
	cnt+=1

print (cnt)
