import numpy as np
import powerlaw

freqs=np.loadtxt("../../gen/visit_freq/visit_freq.csv",dtype=np.int,delimiter=",",skiprows=1)
fw = open("../../gen/visit_freq/visit_freq_powerlaw.csv","w")
fw.write("1-151,alpha,sigma\n")
for shop in freqs:
	fw.write(str(shop[0]))
	fit=powerlaw.Fit(shop[2:],discrete=True)
	alpha = fit.power_law.alpha
	sigma = fit.power_law.sigma

	fw.write(",%f,%f\n"%(alpha,sigma)) 
fw.close()