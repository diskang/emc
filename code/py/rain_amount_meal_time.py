from db import cursor




def get_rain_between(start,end):
	rain_amount = """
select convert(varchar,recordtime, 23) as day ,min(temperature) as minT,max(temperature) as maxT,sum(rain) as allrain  
from weather
where day between '2014-09-01' and '2015-01-31'
group by convert(varchar,recordtime, 23)
having convert(varchar,recordtime, 108) between %s and %s
"""%(start,end)
	cursor.execute(freq_per_times)
	res=cursor.fetchall()
	return res


cursor.close()

