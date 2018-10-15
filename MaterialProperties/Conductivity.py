from math import log10, fabs, floor
import numpy as np
import matplotlib.pyplot as plt
'''
Adding Material Properties files/library's myself

'''

def Inconel_718(T):
    a = -8.28921
    b =  39.4470
    c = -83.4353
    d = 98.1690
    e = -67.2088
    f = 26.7082
    g = -5.7205
    h = 0.51115
    i = 0
    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def AL_ALY_1100(T):
    a= 23.39172
    b= - 148.5733
    c=  422.1917
    d= -653.6664
    e=   607.0402
    f= - 346.152
    g=   118.4276
    h= - 22.2781
    i=   1.770187
    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def AL_ALY_3003F(T):
    a= 0
    b= 0
    c= 0
    d= 0
    e= 0
    f= 0
    g= 0
    h= 0
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


#-------------------------------------------bleh
#script for testing and plotting each function
StartT = 6
EndT = 300
Step = floor(fabs(StartT-EndT)+1)
print(Step)
T = np.linspace(StartT,EndT,Step)
K = np.zeros((Step,1))
#print(T)
for i in range(len(K)):
    K[i] = AL_ALY_1100(T[i])
    #print(T[i], K[i][0])
#K = Inconel_718(T)
#print(K)
figure = plt.figure()
ax = figure.add_subplot(111)
ax.plot(T,K)
plt.show()