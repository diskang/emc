f=open("../../gen/visit_freq/visit_freq.csv")
fw = open("../../gen/visit_freq/visit_freq_statistic.csv","w")
lines = f.readlines()

inteval_list = (range(1,2),range(2,4),range(4,10),range(10,30),range(30,150))
write_buffer = ""
for line in lines[1:]:
	number_in_list = line.split(',')
	accountcode = number_in_list[0]
	write_buffer+=accountcode

	for inteval in inteval_list:
		total_freq = 0
		for freq in inteval:
			freq_visit = number_in_list[freq]
			if freq_visit.isnumeric():
				total_freq +=int(freq_visit)
		write_buffer+=","+str(total_freq)
	write_buffer+="\n"

fw.write(write_buffer)
f.close()
fw.close()