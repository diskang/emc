# in a whole semaster or a single day

from db import cursor
from toaccount import *

"""select toaccount,count(distinct fromaccount) from trade
group by toaccount"""
def list_to_dict(lst):#[(1,2),(a,b),...]=>{1:2,a:b}
	d = dict()
	for i in lst:
		d[i[0]]=i[1]
	return d

def get_from_db():
	query="""
select toaccount,count(fromaccount) from trade
group by toaccount
"""
	cursor.execute(query)
	res=cursor.fetchall()
	return list_to_dict(res)

fw = open("../../gen/active_people_count/customer_per_shop.csv","w")
shop_customers = get_from_db()
for code in account_1 +account_2 +account_3 +account_4 +account_5 +account_6 +coffee  +market+bath:
	customer_count = shop_customers.get(code,0)
	name = account_name.get(code)
	fw.write("%s,%s,%d\n"%(code,name,customer_count))

fw.close()




