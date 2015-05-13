# -*- coding: utf-8 -*-
import pymongo
import time

resultFile = open("result_5min.csv",'w')

client = pymongo.MongoClient('localhost', 27017)
db = client.EMC

ondday = 24*60*60*1000
onemin = 60*1000
starttime = 1413129600*1000
endtime = 1413734399*1000
totallast = endtime - starttime
period = 5*onemin
totalperiod = int(totallast/period)


for i in range(totalperiod):
	if (i%100==0):
		print (i/totalperiod*100)
	periodstart = starttime+(period*i)
	periodend = starttime+(period*(i+1))
	timerange = {'$gte':periodstart,'$lte':periodend}
	for addr in ['1','2','3','4','5','6']:
		addrcnt = 0
		query = {'tradeaddr':addr,'time':timerange}
		results = db.results.find(query)
		calc_result = {'start':periodstart,'end':periodend,'addr':addr,'beforecnt':0,'beforetotal':0,'beforeavr':0,'aftercnt':0,'aftertotal':0,'afteravr':0}
		for result in results:
			if  (result['timediff1']>0):
				addrcnt+=1
				calc_result['beforecnt'] = calc_result['beforecnt']+1
				calc_result['beforetotal'] = calc_result['beforetotal'] + result['timediff1']
			if  (result['timediff2']<0):
				addrcnt+=1
				calc_result['aftercnt'] = calc_result['aftercnt']+1
				calc_result['aftertotal'] = calc_result['aftertotal'] + result['timediff2']
		if (calc_result['beforecnt']>0):
			calc_result['beforeavr'] = calc_result['beforetotal']/calc_result['beforecnt']
		if (calc_result['aftercnt']>0):
			calc_result['afteravr'] = calc_result['aftertotal']/calc_result['aftercnt']
		if  (addrcnt>5):
			# db.calc_results.save(calc_result)
			timestr = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(calc_result['start']/1000))
			resultFile.write(str(calc_result['start'])+","+timestr+","+calc_result['addr']+","+str(addrcnt)+","+str(calc_result['beforeavr']/onemin)+","+str(calc_result['afteravr']/onemin)+"\n")

print ("finish")