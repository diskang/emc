import numpy as np

f=open("../../gen/spend_amount_per_perchase_lunch_dinner.csv")
fw = open("../../gen/spend_amount_count_peak.csv","w")
lines=f.readlines()
for line in lines:
	amount_count_per_shop= line.split(",")
	shop = amount_count_per_shop[0]
	amount_count_per_shop = [int(i) for i in amount_count_per_shop[1:]]
	max_count = max(amount_count_per_shop)
	max_count_amount = amount_count_per_shop.index(max_count)
	fw.write("%s,%d,%d\n"%(shop,max_count_amount,max_count))
	
f.close()
fw.close()
