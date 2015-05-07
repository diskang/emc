from db import cursor
import datetime
all_account=['1000001','1000002','1000003','1000005','1000006','1000007','1000010','1000011','1000014','1000015','1000016','1000019','1000027','1000029','1000030','1000031','1000037','1000038','1000039','1000040','1000041','1000047','1000055','1000056','1000057','1000060','1000061','1000062','1000091','1000092','1000093','1000095','1000098','1000101','1000103','1000105','1000108','1000125','1000127','1000132','1000136','1000137','1000143','1000157','1000159','1000175','1000176','1000178','1000179','1000180','1000181','1000182','1000183','1000184','1000185','1000186','1000187','1000190','1000191','1000193','1000194','1000195','1000202','1000204','1000210','1000211','1000212','1000213','1000215','1000216','1000219','1000220','1000221','1000222','1000231','1000232','1000233','1000236','1000237','1000239','1000240','1000241','1000242','1000244','1000246']

def get_from_db(accountcode,date):
	daily_amount_per_shop = """
select left(convert(nvarchar(19),[timestamp],120),19) from dbo.trade
where toaccount='%s' and left(convert(nvarchar(10),[timestamp],120),10)=left('%s',10)
order by [timestamp]
"""%(accountcode,str(date))
	cursor.execute(daily_amount_per_shop)
	res=cursor.fetchall()
	return res


for acc in all_account:
 	with open("../../gen/trade_frequency_shop/%s.csv"%acc,"w") as f:
 		date=datetime.datetime(2014,9,1,0,0,0)
 		while (date!=datetime.datetime(2015,2,1,0,0,0)):
 			txt=list(get_from_db(acc,date))
			f.write(((((str(txt)).replace('(u','')).replace(',)','')).replace('[','')).replace(']','')[23:]+'\n')
			txt2=txt[:]
			l=[]
			for i in range (len(txt2)-1,0,-1):
				txt2[i]=txt2[i-1]
			for j in range (1,len(txt2)):
				a=datetime.datetime.strptime(((((str(txt[j])).replace('(u','')).replace(',)','')).replace('[','')).replace(']','')[1:20], "%Y-%m-%d %H:%M:%S")
				b=datetime.datetime.strptime(((((str(txt2[j])).replace('(u','')).replace(',)','')).replace('[','')).replace(']','')[1:20], "%Y-%m-%d %H:%M:%S")
				print (a-b).seconds
				f.write(','+'%s'%(a-b).seconds)
			f.write('\n')
			date=date + datetime.timedelta(days=1)

# f=open("../../gen/trade_frequency_shop/%s.csv"%'1000001',"w+")
# date=datetime.datetime(2014,9,1,0,0,0)
# while (date!=datetime.datetime(2015,2,1,0,0,0)):
# 	txt=list(get_from_db('1000001',date))
# 	# print txt
# 	f.write(((((str(txt)).replace('(u','')).replace(',)','')).replace('[','')).replace(']','')+'\n')
# 	txt2=txt[:]
# 	l=[]
# 	for i in range (len(txt2)-1,0,-1):
# 		txt2[i]=txt2[i-1]
# 	for j in range (1,len(txt2)):
# 		a=datetime.datetime.strptime(((((str(txt[j])).replace('(u','')).replace(',)','')).replace('[','')).replace(']','')[1:20], "%Y-%m-%d %H:%M:%S")
# 		b=datetime.datetime.strptime(((((str(txt2[j])).replace('(u','')).replace(',)','')).replace('[','')).replace(']','')[1:20], "%Y-%m-%d %H:%M:%S")
# 		print (a-b).seconds
# 		f.write(','+'%s'%(a-b).seconds)
# 	f.write('\n')
# 	date=date + datetime.timedelta(days=1)

cursor.close()