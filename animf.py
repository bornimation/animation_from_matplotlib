import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.rcParams.update({
    'text.usetex': True,
	'font.family': 'sans-serif',
	'font.sans-serif': ['Helvetica']})
plt.rcParams.update({
	'text.usetex': True,
	'font.family': 'serif',
	'font.serif': ['Palatino'],
	'font.size':16,})
x_l = 0.1
x_u = 30
y_l = -10
y_u = 10
Time = 5
fps = 24
from fdiv import N,p
plt119= plt.figure(119)
y = p(N(x_l,x_u,fps,Time)[0:119])
plt.plot(N(x_l,x_u,fps,Time)[0:119],y,linewidth=2)
plt.xlim(0.1,30)
plt.ylim(-10,10)
plt.savefig('image119.png')
print('frame number',119)
