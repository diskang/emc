# -*- coding: utf-8 -*-
import pymongo
import time

client = pymongo.MongoClient('202.120.38.225', 27017)
db = client.EMC

netUsersFile = open("net_users.dat")
for line in netUsersFile :
	userArr = line.strip().split(',')
	user = {}
	user['user_id'] = int(userArr[0])
	user['gender'] = int(userArr[1])
	user['birth_year'] = int(userArr[2])
	user['grade_year'] = int(userArr[3])
	db.net_users.save(user)

print ("user finish")

netTrafficFile = open("net_traffic.dat", encoding="utf-8")
for line in netTrafficFile :
	trafficArr = line.strip().split(',')
	traffic = {}
	traffic['user_id'] = int(trafficArr[0])
	traffic['location'] = trafficArr[1]
	traffic['start_time'] = int(trafficArr[2])
	traffic['session_duration'] = int(trafficArr[3])
	traffic['service_provider'] = trafficArr[4]
	traffic['service_category'] = trafficArr[5]
	traffic['service_domain'] = trafficArr[6]
	traffic['bytes'] = trafficArr[7]
	traffic['requests'] = trafficArr[8]	
	db.net_trafic.save(traffic)

print ("traffic finish")