# Roger Sheu
# Isotope mass predictor

# Initially made for C12H36O4Si5 (L5 Siloxane), but should be useful for other compounds

# Put in parent species, not ion.

# Output: Writes distribution of isotope ions (by mass) to isotope_dist.csv (in root directory)

# Future coding option: Include formulas in a separate column

# Future development: Either get user input (parse a chemical formula) or accept flags.

import numpy as np
import pandas as pd
import random

def isotope_distribution(numC, numH, numN, numO, numS, numSi):
	C12Mass = 12
	C13Mass = 13.00335
	HMass = 1.00782
	DMass = 2.0141
	O16Mass = 15.9949
	O18Mass = 17.9992
	N14Mass = 14.0031
	N15Mass = 15.0001
	S32Mass = 31.9721
	S34Mass = 33.9679
	Si28Mass = 27.9769
	Si29Mass = 28.9765
	Si30Mass = 29.9738
	C12Prevalence = .9893
	C13Prevalence = .0107
	HPrevalence = .999885
	DPrevalence = .000115
	O16Prevalence = .9976
	O18Prevalence = .00205
	N14Prevalence = .9964
	N15Prevalence = .00364
	S32Prevalence = .9499
	S34Prevalence = .0425
	Si28Prevalence = .9222
	Si29Prevalence = .04685
	Si30Prevalence = .03092
	
	IonMass = 1.007276
	
	
	masses = []
	
	for i in range(10000):
		totMass = 0
		
		for c in range(numC):
			if random.random() < C13Prevalence:
				totMass += C13Mass
			else:
				totMass += C12Mass
		
		for h in range(numH):
			if random.random() < DPrevalence:
				totMass += DMass
			else:
				totMass += HMass
				
		for n in range(numN):
			if random.random() < N15Prevalence:
				totMass += N15Mass
			else:
				totMass += N14Mass
			
		for o in range(numO):
			if random.random() < O18Prevalence:
				totMass += O18Mass
			else:
				totMass += O16Mass
				
		for s in range(numS):
			if random.random() < S34Prevalence:
				totMass += S34Mass
			else:
				totMass += S32Mass
		
		for si in range(numSi):
			if random.random() < Si30Prevalence:
				totMass += Si30Mass
			elif random.random() < Si30Prevalence + Si29Prevalence:
				totMass += Si29Mass
			else:
				totMass += Si28Mass
		
		
		totMass += IonMass
		
		totMass = round(totMass,5)
		
		
		masses.append(totMass)
	
	df = pd.DataFrame(masses, columns=['masses'])
	# df2 = df.sort_values(by="masses",ascending=True)
	
	# Changes the index axis to a new column and changes the original 
	df2 = df['masses'].value_counts().rename_axis('mass').reset_index(name='counts')
	
	
	# Filter out unimportant outcomes
	min = df2.iloc[0,1] * 0.01
	df2 = df2[df2['counts'] > min]
	
	df2.to_csv("isotope_dist.csv")
	
# C,H,N,O,S,Si
isotope_distribution(14,42,0,7,0,7)
	
