import math

flowRate = 5.0 # m3/s
tankHeight = 5 # m
tankRadius = 10 # m
pi = 3.14159 
tankArea = pi * (tankRadius**2) # pi * r**2
T = 300 # sec (5 min)
td = 1 # time differential
vTank = tankArea * tankHeight
vLiq = 0
drainRadius = .5 # m
drainArea = pi * (drainRadius**2) # pi * r**2

for i in range(T):
    vLiq = vLiq + (flowRate * td) 
    
    hLiq = max(vLiq / tankArea, 0) # height = v / pi * r**2, can't be below 0
    
    vDrain = drainArea * math.sqrt(2 * 9.81 * hLiq) # V = Cd A (2 g H)1/2  ?? Matworks divided by the total tank area?
    
    vLiq = max(vLiq - (vDrain / td), 0)
        
    if i % 10 == 1:
        print("current time: " + str(i) + " and height: " + str(vLiq) + " and vDrain: " + str(vDrain))

    if vLiq > vTank:
        print("overflow!!")
        break

