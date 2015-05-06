from db import cursor
from toaccount import all_account
#cursor.execute("select count(*) from trade")#7915289

#cursor.execute("select max(timestamp) from trade where toaccount=1000244 and syscode=36" )
# cursor.execute("select min(timestamp) from trade where toaccount=1000244 and syscode=268" )

def get_from_db(accountcode):
	daily_amount_per_shop = """select  convert(varchar,timestamp, 23) as day ,sum(amount) as total
from trade 
where toaccount='%s' 
group by toaccount, convert(varchar,timestamp, 23) 
order by day
"""%accountcode
	cursor.execute(daily_amount_per_shop)
	res=cursor.fetchall()
	return res

for acc in all_account:
	with open("../../gen/amount_per_day_shop/%s.csv"%acc,"w") as f:
		amount_per_day = get_from_db(acc)
		for i in amount_per_day:
			f.write("%s,%s\n"%(str(i[0]),str(i[1])))
	
cursor.close()