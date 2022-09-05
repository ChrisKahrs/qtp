import math

# Single Tank, everything in meters and seconds 

class Tank():
    def __init__(self) -> None:
       
        self.vFlowRate = 15.0 # m3/s
        self.gamma = 0.0 # % flow rate going to tank
        self.tankHeight = 5 # m
        self.tankRadius = 10 # m
        self.pi = 3.14159 
        self.tankArea = self.pi * (self.tankRadius**2) # area = pi * r**2
        self.td = 0.1 # time differential per control loop
        self.T = math.floor(60 / self.td) # sec (1 min)
        self.vTank = self.tankArea * self.tankHeight # volume of tank (m3)
        self.vLiq = 0 # volume of liquid in tank (m3)
        self.drainRadius = .5 # m
        self.drainArea = self.pi * (self.drainRadius**2) # area = pi * r**2
        self.g = 9.81 # m/s2
        self.hLiq = 0 # m 
        self.overflowed = False
        self.emptied = False
        self.vIn = 0 # m3
        self.vDrain = 0 # m3
        self.hSetPoint = 0 # m

    def step(self):
            
        self.vIn = ((self.vFlowRate * self.gamma) * self.td) + self.vIn  ## m3 = (m3/s * s) + m3
        
        self.vLiq = self.vLiq + self.vIn # add flowrate to volume of liquid in tank  ## m3 = (m3 + m3)
        
        self.hLiq = max(self.vLiq / self.tankArea, 0) # height of Liquid = v / pi * r**2, can't be below 0  ## m = (m3 / pi*m2 )
        
        self.vDrain = self.drainArea * math.sqrt(2 * self.g * self.hLiq) * self.td # V = Cd A (2 g H)1/2 * timeDelta   ## m3 = (m2 * sqrt(m/s2 * m) * s)

        self.vLiq = max(self.vLiq - self.vDrain, 0) # take away the volume of the drain from the volume of the liquid  ## m3 = (m3 - m3)
        
        if self.vLiq > self.vTank:
           self.overflowed = True
        elif self.vLiq == 0:
           self.emptied = True

blt = Tank()
blt.gamma = 0.7
brt = Tank()
brt.gamma = 0.7
tlt = Tank()
tlt.gamma = 0.3
trt = Tank()
trt.gamma = 0.3
           
for i in range(brt.T):
    tlt.vIn = 0
    tlt.step()
    blt.vIn = tlt.vDrain
    blt.step()
    
    trt.vIn = 0
    trt.step()
    brt.vIn = trt.vDrain
    brt.step()
    
        
    if i % 10 == 1:
        print("current time: " + str(i) + " and blt height: " + str(blt.hLiq))
        print("current time: " + str(i) + " and brt height: " + str(brt.hLiq))
        print("current time: " + str(i) + " and tlt height: " + str(tlt.hLiq))
        print("current time: " + str(i) + " and trt height: " + str(trt.hLiq))
        print("____________________________________________")
        

    # if tank.overflowed:
    #     print("overflow!!")
    #     break
    # elif tank.emptied:
    #     print("emptied!!")
    #     break

