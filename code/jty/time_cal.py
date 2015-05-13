# -*- coding: utf-8 -*-
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
db = client.EMC

userColle = db.account.find()

# resultFile = open("result.txt","w")
cnt=0
for user in userColle:
	query1 = {'studentcode':str(user['studentcode']),'addr':{'$ne':'x'},'timestamp':{'$gte':1413129600000,'$lte':1413734399000}}
	# query1 = {'studentcode':str(user['studentcode']),'addr':{'$ne':'x'}}
	trades = db.trade.find(query1)
	for trade in trades:
		addrc = ""
		if (trade['addr'] == '1'):
			addrc = "第一食堂"
		elif (trade['addr'] == '2'):
			addrc = "第二食堂"
		elif (trade['addr'] == '3'):
			addrc = "第三食堂"
		elif (trade['addr'] == '4'):
			addrc = "第四食堂"
		elif (trade['addr'] == '5'):
			addrc = "第五食堂"
		elif (trade['addr'] == '6'):
			addrc = "第六食堂"
		query2 = {'user_id':user['studentcode'],'start_time':{'$gte':trade['timestamp']-(1000*60*60),'$lte':trade['timestamp']+(1000*60*60)},'location':addrc}
		traffics = db.net_trafic.find(query2)
		for traffic in traffics:
			# resultFile.write('trade:'+"sid:"+trade['studentcode']+"tradetime:"+str(trade['timestamp'])+"tradeaddr:"+trade['addr'])
			# print('trade:'+"sid:"+trade['studentcode']+"tradetime:"+str(trade['timestamp'])+"tradeaddr:"+trade['addr'])
			# resultFile.write(str(traffic['user_id'])+traffic['location']+str(traffic['start_time'])+str(traffic['session_duration']))
			# resultFile.write('traffic:'+"sid:"+str(traffic['user_id'])+"trafficstart"+str(traffic['start_time'])+"trafficdur"+str(traffic['session_duration']))
			# print('traffic:'+"sid:"+str(traffic['user_id'])+"trafficstart"+str(traffic['start_time'])+"trafficdur"+str(traffic['session_duration']))
			timediff1 = trade['timestamp'] - traffic['start_time']
			timediff2 = trade['timestamp'] - (traffic['start_time'] + traffic['session_duration'])
			timestr = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(trade['timestamp']/1000))
			# print({'user_id':traffic['user_id'],"timestr":timestr,"timediff1":timediff1,"timediff2":timediff2,"tradeaddr":trade['addr']})
			result = {'user_id':traffic['user_id'],"time":trade['timestamp'],"timestr":timestr,"timediff1":timediff1,"timediff2":timediff2,"tradeaddr":trade['addr'],'trade':trade,'traffic':traffic}
			db.results.save(result)
	if (cnt%20==0):
		print (cnt/30861*100)
	cnt+=1
# tradeColle = db.trade.find()

# for trade in tradeColle:
# 	query = {'user_id':trade['studentcode']}
# 	# query = {'user_id':trade['studentcode'],'start_time':{'$gte':trade['timestamp']-(24*1000*60*60),'$lte':trade['timestamp']+(24*1000*60*60)}}
# 	# print (query)
# 	for traffic in db.net_trafic.find(query):
# 		print (traffic['start_time'])
# 		print (trade)

print ("trade finish")