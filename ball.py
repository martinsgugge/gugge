from numpy import linspace
import matplotlib.pyplot as plt



v0=5                 #Initial velocity
g=9.81
t=linspace(0,1,1001) #Gir 1000 intervaller, 1001 punkter

y=v0*t-0.5*g*t**2
print(y)

plt.plot(t,y)
plt.xlabel('time[s]')
plt.ylabel('height[m]')
plt.show()