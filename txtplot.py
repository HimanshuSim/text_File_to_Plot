import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def gaussian(x,mu,c,a):
    return a*np.exp(-((x-mu)**2)/((c**2)))

fname=input("Enter the name of the input file: ")
inp=input("what columns you want to plot ")#pass input as colxno colyno additional
cols=inp.split()

###
try:
    fhand=open(fname)
except:
    print(" Can't find the file ")
    quit()

def file_parse(colno):
    filem=list()
    filem2=list()

    for line in fhand:
        elem=list()
        elem=line.split()
        if elem[int(colno[0])]!='NaN' and elem[int(colno[1])]!='NaN':
            filem.append(np.float_(elem[int(colno[0])]))
            filem2.append(np.float_(elem[int(colno[1])]))
    fhand.seek(0)
    return(filem,filem2)

x1,y1=np.array(file_parse(cols[0:2]))
#x2,y2=np.array(file_parse(cols[2:4]))
#x3,y3=np.array(file_parse(cols[4:6]))
fhand.close()


def fit_param(x,y):
    a=max(y)
    mu=x[int(np.where(y==a)[0])] # mean(x)
    sig=np.std(x)
    return (a, mu, sig)
def zero_der(x,y):
    h=x[1]-x[0]
    d=list()
    for i in range(1,len(y)-3):
        if (y[i]-y[i-1])/(h)>(y[i+1]-y[i-1])/(2*h)+h*2:
            d.append(y[i])
    return np.array(d) 


xmin=53
xmax=58
lstx=list()
lsty=list()
for i in range(len(x1)):
    if x1[i]>xmin and x1[i]<xmax:
        lstx.append(x1[i])
        lsty.append(y1[i])
plt.ylabel(r"Intensity")
plt.xlabel(r"2$\theta$")
plt.title(r'Intensity vs 2$\theta$ ({} peak) '.format(cols[-1]))
plt.grid(alpha=0.6)
plt.plot(lstx,lsty)

plt.text(56.0,max(lsty)/2+5,'(56.49)')
plt.text(56.95,max(lsty)/2+5,'(56.94)')
#plt.text(36.9,4.12e3,'(36.3)')

plt.axhline(y=max(lsty)/2, color='limegreen')

plt.legend()
plt.show()
