from math import log10, fabs, floor
import numpy as np
import matplotlib.pyplot as plt
'''
Adding Material Properties files/library's myself

'''

def Inconel_718(T):
    # [W/(m-K)]
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
    # [W/(m-K)]
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


def AL_ALY_3003(T):
    # [W/(m-K)]
    a= 0.63736
    b= -1.1437
    c= 7.4624
    d= -12.6905
    e= 11.9165
    f= -6.18721
    g= 1.63939
    h= -0.172667
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def AL_ALY_5083(T):
    # [W/(m-K)]
    a= -0.90933
    b= 5.751
    c= -11.112
    d= 13.612
    e= -9.3977
    f= 3.6873
    g= -0.77295
    h= 0.067336
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def AL_ALY_6061_T6(T):
    # [W/(m-K)]
    a=0.07918
    b=1.0957
    c=-0.07277
    d=0.08084
    e=0.02803
    f=-0.09464
    g=0.04179
    h=-0.00571
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans

def AL_ALY_6063_T5(T):
    # [W/(m-K)]
    a=22.401433
    b=-141.13433
    c=394.95461
    d=-601.15377
    e=547.83202
    f=-305.99691
    g=102.38656
    h=-18.810237
    i= 1.4576882

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def Balsa_lowdensity(T):
    #(density = 6 lb/ft3)
    # [W/(m-K)]
    a=4172.447
    b=-11309.97
    c=12745.09
    d=-7647.584
    e=2577.309
    f=-462.538
    g=34.5351
    h=0
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def Balsa_highdensity(T):
    #(density = 11 lb/ft3)
    # [W/(m-K)]
    a=4815.4
    b=-12969.63
    c=14520.76
    d=-8654.164
    e=2895.712
    f=-515.7272
    g=38.19218
    h=0
    i=0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def Beechwood_Phenolic_0(T):
    # (cross-laminate [0/90], grain direction)
    # Data Range: 92-300
    # Equation Range: 80-300
    # Curve Fit % error relative to data: 1
    # [W/(m-K)]
    a=-1375.11
    b=3740.69
    c=3740.69
    d=2559.333
    e=-868.6067
    f=157.1018
    g=-11.82957
    h= 0
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def Beechwood_Phenolic_90(T):
    # (cross-laminate [0/90], flatwise)
    # Data Range: 92-300
    # Equation Range: 75-300
    # Curve Fit % error relative to data: 1.5
    # [W/(m-K)]
    a=1035.33
    b=-2191.85
    c=1470.505
    d=39.845
    e=-541.9035
    f=289.844
    g=-65.2253
    h=5.59956
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans


def Beryllium_Copper(T):
    # Common Spring material
    # Data Range: 2-80
    # Equation Range: 1-120
    # Curve Fit % error relative to data: 2
    # [W/(m-K)]
    a=-0.50015
    b=1.93190
    c=-1.69540
    d=0.71218
    e=1.27880
    f=-1.61450
    g=0.68722
    h=-0.10501
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans



'''

def Balsa_lowdensity(T):
    # (cross-laminate [0/90], flatwise)
    # Data Range: 92-300
    # Equation Range: 75-300
    # Curve Fit % error relative to data: 1.5
    # [W/(m-K)]
    a=
    b=
    c=
    d=
    e=
    f=
    g=
    h=
    i= 0

    y1 = a+b*(log10(T)) + c*(log10(T))**2 + d*(log10(T))**3 + e*(log10(T))**4
    y2 = f*(log10(T))**5 + g*(log10(T))**6 + h*(log10(T))**7 + i*(log10(T))**8
    ans = 10**(y1+y2)
    return ans
    
    
    
'''
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
    K[i] = AL_ALY_5083(T[i])
    #print(T[i], K[i][0])
#K = Inconel_718(T)
#print(K)
figure = plt.figure()
ax = figure.add_subplot(111)
ax.plot(T,K)
plt.show()