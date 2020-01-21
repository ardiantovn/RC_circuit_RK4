import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
#charging

def rk_charge(h,N,R,C,V_0,V):
    k1=(V_0-V)/(R*C)
    k2=(V_0-(V+h*0.5*k1))/(R*C)
    k3=(V_0-(V+h*0.5*k2))/(R*C)
    k4=(V_0-(V+h*k3))/(R*C)
    V=V+(k1+2*k2+2*k3+k4)*h/6
    return V

R=1000 #ohm
C=0.001#F
V_0=3.3 #V
N=10
x,y=[],[]
h=0.1
for i in np.arange(0,N,h):
    if i==0:
        V=0
    else:
        V=rk_charge(h,N,R,C,V_0,V)
    x.append(i)
    y.append(V)
plt.figure(figsize=(8,6))
plt.plot(x,y)
plt.show() 
