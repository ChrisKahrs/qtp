import math

# Single Tank, everything in meters and seconds 

class tank():
    def __init__(self) -> None:
       
        self.vFlowRate = 15.0 # m3/s
        self.tankHeight = 5 # m
        self.tankRadius = 10 # m
        self.pi = 3.14159 
        self.tankArea = self.pi * (self.tankRadius**2) # area = pi * r**2
        self.td = 0.1 # time differential per loop
        self.T = math.floor(300 * 1/td) # sec (5 min)
        self.vTank = self.tankArea * self.tankHeight # volume of tank (m3)
        self.vLiq = 0 # volume of liquid in tank (m3)
        self.drainRadius = .5 # m
        self.drainArea = self.pi * (self.drainRadius**2) # area = pi * r**2
        self.g = 9.81 # m/s2

    def step(self, action) -> dict:
    vIn = vFlowRate * td   ## m3 = (m3/s * s)
    
    vLiq = vLiq + vIn # add flowrate to volume of liquid in tank  ## m3 = (m3 + m3)
    
    hLiq = max(vLiq / tankArea, 0) # height of Liquid = v / pi * r**2, can't be below 0  ## m = (m3 / pi*m2 )
    
    vDrain = drainArea * math.sqrt(2 * g * hLiq) * td # V = Cd A (2 g H)1/2 * timeDelta??   ## m3 = (m2 * sqrt(m/s2 * m) * s)

    vLiq = max(vLiq - vDrain, 0) # take away the volume of the drain from the volume of the liquid  ## m3 = (m3 - m3)
        
    if i % 10 == 1:
        print("Time: " + str(i) + ", hLiq: " + str(hLiq) + ", vLiq: " + str(vLiq) + ", vDrain: " + str(vDrain))

    if vLiq > vTank:
        print("overflow!!")
        break

