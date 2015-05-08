from db import cursor
from toaccount import *

def get_from_db():
	active_people_per_day = """select  convert(varchar,timestamp, 23) as day ,count(distinct fromaccount)
from trade 
where convert(varchar,timestamp, 108) between '16:30:00' and '19:00:00'
group by convert(varchar,timestamp, 23) 
order by day
"""
	cursor.execute(active_people_per_day)
	res=cursor.fetchall()
	return res

def get_from_db_per_group(group):
	active_people_per_group = """select  convert(varchar,timestamp, 23) as day ,count(distinct fromaccount)
from trade 
where toaccount in %s and convert(varchar,timestamp, 108) between '16:30:00' and '19:00:00'
group by convert(varchar,timestamp, 23) 
order by day
"""%str(group)
	cursor.execute(active_people_per_group)
	res=cursor.fetchall()
	return res

def list_to_dict(lst):#[(1,2),(a,b),...]=>{1:2,a:b}
	d = dict()
	for i in lst:
		d[i[0]]=i[1]
	return d

with open("../../gen/active_people_count/per_dinner.csv","w") as f:
	per_day_list = get_from_db()
	per_day_dict = list_to_dict(per_day_list)

	active1 = get_from_db_per_group(account_1)
	active1 = list_to_dict(active1)
	# print (per_day_dict)
	active2 = get_from_db_per_group(account_2)
	active2 = list_to_dict(active2)
	active3 = get_from_db_per_group(account_3)
	active3 = list_to_dict(active3)
	active4 = get_from_db_per_group(account_4)
	active4 = list_to_dict(active4)
	active5 = get_from_db_per_group(account_5)
	active5 = list_to_dict(active5)
	active6 = get_from_db_per_group(account_6)
	active6 = list_to_dict(active6)
	#title
	f.write("day,all,1,2,3,4,5,6\n")
	for i in per_day_list:
		day = i[0]
		count0=per_day_dict.get(day,0)
		count1=active1.get(day,0)
		count2=active2.get(day,0)
		count3=active3.get(day,0)
		count4=active4.get(day,0)
		count5=active5.get(day,0)
		count6=active6.get(day,0)
		print(count0,count1)
		f.write("%s,%d,%d,%d,%d,%d,%d,%d\n"%(day,count0,count1,count2,count3,count4,count5,count6
			))
cursor.close()
