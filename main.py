import math

# Single Tank, everything in meters and seconds 

class Tank():
    def __init__(self) -> None:
       
        self.vFlowRate = 15.0 # m3/s
        self.tankHeight = 5 # m
        self.tankRadius = 10 # m
        self.pi = 3.14159 
        self.tankArea = self.pi * (self.tankRadius**2) # area = pi * r**2
        self.td = 0.1 # time differential per loop
        self.T = math.floor(60 / self.td) # sec (1 min)
        self.vTank = self.tankArea * self.tankHeight # volume of tank (m3)
        self.vLiq = 0 # volume of liquid in tank (m3)
        self.drainRadius = .5 # m
        self.drainArea = self.pi * (self.drainRadius**2) # area = pi * r**2
        self.g = 9.81 # m/s2
        self.hLiq = 0 # m 
        self.overflowed = False
        self.emptied = False

    def step(self):
            
        vIn = self.vFlowRate * self.td   ## m3 = (m3/s * s)
        
        self.vLiq = self.vLiq + vIn # add flowrate to volume of liquid in tank  ## m3 = (m3 + m3)
        
        self.hLiq = max(self.vLiq / self.tankArea, 0) # height of Liquid = v / pi * r**2, can't be below 0  ## m = (m3 / pi*m2 )
        
        vDrain = self.drainArea * math.sqrt(2 * self.g * self.hLiq) * self.td # V = Cd A (2 g H)1/2 * timeDelta   ## m3 = (m2 * sqrt(m/s2 * m) * s)

        self.vLiq = max(self.vLiq - vDrain, 0) # take away the volume of the drain from the volume of the liquid  ## m3 = (m3 - m3)
        
        if self.vLiq > self.vTank:
           self.overflowed = True
        elif self.vLiq == 0:
           self.emptied = True

tank = Tank()
           
for i in range(tank.T):
    tank.step()
        
    if i % 10 == 1:
        print("current time: " + str(i) + " and height: " + str(tank.hLiq))

    if tank.overflowed:
        print("overflow!!")
        break
    elif tank.emptied:
        print("emptied!!")
        break

