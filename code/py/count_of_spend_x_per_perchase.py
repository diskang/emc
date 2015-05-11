from db import cursor
from toaccount import *

"""select (amount/100) as amt, count(amount/100) as perchase_count 
from emc.dbo.trade
where toaccount = '1000029'
group by (amount/100)
order by amt"""

def _list_to_dict(lst):#[(1,2),(a,b),...]=>{1:2,a:b}
	d = dict()
	for i in lst:
		d[i[0]]=i[1]
	return d

def count_of_spend_x_when(start,end,toaccount):
	query ="""
select (amount/100) as amt, count(amount/100) as perchase_count 
from emc.dbo.trade
where toaccount = '%s' and convert(varchar,timestamp, 108) between '%s' and '%s'
group by (amount/100)
order by amt
"""%(toaccount,start,end)
	cursor.execute(query)
	res=cursor.fetchall()
	return _list_to_dict(res)

def count_of_spend_x_when_breakfirst(toaccount):
	return count_of_spend_x_when("05:30:00","10:00:00",toaccount)


def count_of_spend_x_after_breakfirst(toaccount):
	return count_of_spend_x_when("10:30:00","19:00:00",toaccount)

# max_yuan=16
# fw = open("../../gen/spend_amount_per_perchase_breakfirst.csv","w")
# fw.write(","+",".join([str(i) for i in range(max_yuan)])+"\n")
# for code in account_1 +account_2 +account_3 +account_4 +account_5 +account_6 +coffee  +market+bath:
# 	breakfirst_spend = count_of_spend_x_when_breakfirst(code)
# 	line = account_name[code]
# 	for spend in range(max_yuan):
# 		spend_count = breakfirst_spend.get(spend,0)
# 		line+=","+str(spend_count)
# 	line+="\n"

# 	fw.write(line)

max_yuan=30
fw = open("../../gen/spend_amount_per_perchase_lunch_dinner.csv","w")
fw.write(","+",".join([str(i) for i in range(max_yuan)])+"\n")
for code in account_1 +account_2 +account_3 +account_4 +account_5 +account_6 +coffee  +market+bath:
	lunch_dinner_spend = count_of_spend_x_after_breakfirst(code)
	line = account_name[code]
	for spend in range(max_yuan):
		spend_count = lunch_dinner_spend.get(spend,0)
		line+=","+str(spend_count)
	line+="\n"

	fw.write(line)

fw.close() 

