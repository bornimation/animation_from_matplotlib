import numpy as np
import matplotlib.pyplot as plt
def p(y):
	x = np.array(y)
	return np.sqrt(x)*np.log(x)*np.cos(x)
	
def N(a,b,F,T):
	X = []
	for t in range(T):
		for f in range(F):
			X.append(a+t*(b-a)/T+f*(b-a)/(T*F))
	return X
#print(N(0,1,5,10))
