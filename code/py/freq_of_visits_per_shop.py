"""
select student_visit_times,count(*) as freq_of_visit_times from 
	(select count(*)as student_visit_times from emc.dbo.trade 
	where toaccount=1000057
	group by fromaccount)a
group by student_visit_times
"""

from db import cursor
from toaccount import *

def get_freq_per_times(shopcode):
	freq_per_times = """
select student_visit_times,count(*) as freq_of_visit_times from 
	(select count(*)as student_visit_times from emc.dbo.trade 
	where toaccount=%s
	group by fromaccount)a
group by student_visit_times
"""%str(shopcode)
	cursor.execute(freq_per_times)
	res=cursor.fetchall()
	return res

def list_to_dict(lst):#[(1,2),(a,b),...]=>{1:2,a:b}
	d = dict()
	for i in lst:
		d[i[0]]=i[1]
	return d

with open("../../gen/visit_freq/visit_freq.csv","w") as f:
	firstline = ','.join([str(i) for i in range(1,151)])
	f.write(','+firstline+'\n')
	for code in account_1 +account_2 +account_3 +account_4 +account_5 +account_6 +coffee  +market+bath:
		
		freqi_list = get_freq_per_times(code)
		freqi_dict = list_to_dict(freqi_list)
		freq_string=str(code)
		for freq in range(1,151):
			freq_string += ','+str(freqi_dict.get(freq,""))
		freq_string+='\n'
		f.write(freq_string)	
cursor.close()