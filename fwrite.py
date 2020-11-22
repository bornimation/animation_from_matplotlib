import numpy as np
x_l = 0.1
x_u = 30
y_l = -10
y_u = 10

F = 24
T = 5
#Plot_Title = "\\frac{exp(-x)*sin(x)}{x^2+1}"
import os
from fdiv import N

for x in N(x_l,x_u,F,T):
	animfile = open('animf.py','w')
	animfile.writelines("import numpy as np\n")
	animfile.writelines("import matplotlib.pyplot as plt\n")
	animfile.writelines("import matplotlib as mpl\n")
	animfile.writelines("plt.rcParams.update({\n")
	animfile.writelines("    "+"'text.usetex': True,\n")
	animfile.writelines("	"+"'font.family': 'sans-serif',\n")
	animfile.writelines("	"+"'font.sans-serif': ['Helvetica']})\n")
	animfile.writelines("plt.rcParams.update({\n")
	animfile.writelines("	"+"'text.usetex': True,\n")
	animfile.writelines("	"+"'font.family': 'serif',\n")
	animfile.writelines("	"+"'font.serif': ['Palatino'],\n")
	animfile.writelines("	"+"'font.size':16,})\n")
	animfile.writelines("x_l = "+str(x_l)+"\n")
	animfile.writelines("x_u = "+str(x_u)+"\n")
	animfile.writelines("y_l = "+str(y_l)+"\n")
	animfile.writelines("y_u = "+str(y_u)+"\n")		
	animfile.writelines("Time = "+str(T)+"\n")
	animfile.writelines("fps = "+str(F)+"\n")
	animfile.writelines("from fdiv import N,p\n")
	i = N(x_l,x_u,F,T).index(x)
	animfile.writelines("plt"+str(i)+"= plt.figure("+str(i)+")\n")
	animfile.writelines("y = p(N(x_l,x_u,fps,Time)[0:"+str(i)+"])\n")
	animfile.writelines("plt.plot(N(x_l,x_u,fps,Time)[0:"+str(i)+"],y,linewidth=2)\n")
	animfile.writelines("plt.xlim("+str(x_l)+","+str(x_u)+")\n")
	animfile.writelines("plt.ylim("+str(y_l)+","+str(y_u)+")\n")
	#animfile.writelines("plt.title(r'$"+str(Plot_Title)+"$')\n")
	animfile.writelines("plt.savefig('image"+str(i)+".png')\n")
	animfile.writelines("print('frame number',"+str(i)+")\n")
	os.system("python3 animf.py")
#os.system("cd /images")
os.system(" ffmpeg -framerate"+"	"+str(F)+"	"+"-i image%d.png video.webm")
