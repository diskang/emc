import numpy as np
from toaccount import account_name

freqs=np.loadtxt("../../gen/visit_freq/visit_freq.csv",dtype=np.int,delimiter=",",skiprows=1)
fw = open("../../gen/visit_freq/visit_freq_power_scaleY.csv","w")
# fw.write("1-151,alpha,sigma\n")
for shop in freqs:
	shopcode = str(shop[0])
	line = shopcode+","+account_name.get(shopcode,"")
	
	total_people = sum(shop[2:])
	for q in shop[2:]:
		line+=","
		if q<=0:
			continue
		else:
			line+=str((total_people*1.0/q)**0.66)
	line+="\n"		
	fw.write(line) 
fw.close()