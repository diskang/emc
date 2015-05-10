from db import cursor
from datetime import datetime
from datetime import timedelta
from toaccount import *

# X=10 or 30

"""
select b.toaccount, workday_count,number, workday_count*1.0/number from

--get total flow within the time interval
	(select toaccount, count(*) as number
		from emc.dbo.trade  where convert(varchar,timestamp, 108) between '14:00:00' and '15:00:00'
		group by toaccount)a
right outer join

--get get active date count per shop
	(select toaccount,count(distinct convert(varchar,timestamp, 23)) as workday_count
		from emc.dbo.trade 
		group by toaccount)b

on a.toaccount = b.toaccount
"""
START_POINT = datetime(100,1,1,5,30,0)
FINISH_POINT = datetime(100,1,1,23,30,0)
INTERVAL = [10,30]
def list_to_dict(lst):#[(1,2),(a,b),...]=>{1:2,a:b}
	d = dict()
	for i in lst:
		d[i[0]]=i[1]
	return d

def get_shop_flow_between(start,end):
	query = """
select toaccount, count(*) as number
		from emc.dbo.trade  where convert(varchar,timestamp, 108) between '%s' and '%s'
		group by toaccount"""%(start,end)
	print(query)
	cursor.execute(query)
	res=cursor.fetchall()
	return list_to_dict(res)

def get_valid_days_per_shop():
	query="""
select toaccount,count(distinct convert(varchar,timestamp, 23)) as workday_count
		from emc.dbo.trade 
		group by toaccount
	"""
	cursor.execute(query)
	res=cursor.fetchall()
	return list_to_dict(res)

days = get_valid_days_per_shop()
for t in INTERVAL:
	start = START_POINT
	end = START_POINT+ timedelta(seconds=t*60)
	f=open("../../gen/flow/flow_per_%smin.csv"%str(t),"w")
	f.write(','+','.join([str(i) for i in all_account])+"\n")# make 1st column empty
	for i in all_account:
		valid_days= days.get(i,0)
		f.write(","+str(valid_days))
	f.write('\n')
	while end<= FINISH_POINT:
		
		flows = get_shop_flow_between(start.time().isoformat(),end.time().isoformat())
		

		for i in all_account:
			valid_days= days.get(i,0)
			valid_flow = flows.get(i,0)
			if valid_days>0 and valid_flow>0:
				f.write(","+str(valid_flow*1.0/valid_days))
			else:
				f.write(',')
		f.write('\n')


		start = end
		end += timedelta(seconds=t*60)
	f.close()
cursor.close()
