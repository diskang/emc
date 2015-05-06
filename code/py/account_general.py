
from db import cursor


#cursor.execute("select distinct grade from account where type='f'")
# 2007~2014
#cursor.execute("select distinct grade from account where type='b'")
#2001,2006,2007,2010~2015
#cursor.execute("select distinct grade from account where type='a'")
#2004~2014

#for i in ['f','b','a']:
	# cursor.execute("select count(*)from account where type='%s'"%i)
	# cursor.execute("select count(*)from account where type='%s' and gender=1"%i)
	# print str(i)+":"+str(cursor.fetchone())
#f:(15374,male-10154) b:(10492,male-6504) a:(4995,male-3465)
#for i in range(2004,2016):
#	cursor.execute("select count(*) from account where grade=%d"%i)
#	print str(i)+":"+str(cursor.fetchone())
# 2004:6, 2005:4, 2006:10, 2007:71, 2008:197, 2009:481, 2010:1575, 2011:4112, 2012:7469, 2013:8063, 2014:8869, 2015:3


cursor.close()
