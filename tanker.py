from pythonfmu import Fmi2Causality, Fmi2Variability, Fmi2Slave, Real, Boolean, Integer
import math
import random

class Tank():
    def __init__(self, hSetPoint, vFlowrate, vLiq):
        
        self.vFlowRate = vFlowrate # m3/s
        self.gamma = 1 # % flow rate going to tank
        self.td = 0.1 # time differential per control loop
        self.T = math.floor(60 / self.td) # sec (1 min)
        self.pi = 3.14159 
        self.g = 9.81 # m/s2
        
        self.hSetPoint = 0
        self.hLiq = 0
        
        self.tankHeight = 5 # m
        self.tankRadius = 10 # m
        self.tankArea = self.pi * (self.tankRadius**2) # area = pi * r**2
        self.vTank = self.tankArea * self.tankHeight # volume of tank (m3)
        self.vLiq = vLiq # volume of liquid in tank (m3)
        self.drainRadius = 0.65 # m
        self.drainArea = self.pi * (self.drainRadius**2) # area = pi * r**2
        self.hLiq = max(self.vLiq / self.tankArea, 0) # m 
        self.overflowed = False
        self.emptied = False
        self.vIn = 0 # m3
        self.vDrain = 0 # m3
        self.hSetPoint = hSetPoint # m

    def step(self, flowrate):
        
        self.vFlowRate = flowrate
            
        self.vIn = ((self.vFlowRate * self.gamma) * self.td) + self.vIn  ## m3 = (m3/s * s) + m3
        
        self.vLiq = self.vLiq + self.vIn # add flowrate to volume of liquid in tank  ## m3 = (m3 + m3)
        
        self.hLiq = max(self.vLiq / self.tankArea, 0) # height of Liquid = v / pi * r**2, can't be below 0  ## m = (m3 / pi*m2 )
        
        self.vDrain = self.drainArea * math.sqrt(2 * self.g * self.hLiq) * self.td # V = Cd A (2 g H)1/2 * timeDelta   ## m3 = (m2 * sqrt(m/s2 * m) * s)

        self.vLiq = max(self.vLiq - self.vDrain, 0) # take away the volume of the drain from the volume of the liquid  ## m3 = (m3 - m3)
        
        self.vIn = 0 # reset it so simple tank works, but an above tank can set it from it's drain value if configured
        
        if self.vLiq > self.vTank:
           self.overflowed = True
        elif self.vLiq == 0:
           self.emptied = True
           
class TankController():
    def __init__(self, hSetPoint, initialFlow, vLiq,controlFreqMultiplier=1):
        self.mainTank = Tank(hSetPoint, initialFlow, vLiq)
        self.controlFreqMultiplier = controlFreqMultiplier
        self.iterCount = 0
        self.SPChangeDone = False
        
    def step(self, flowrate):    
        for _ in range(self.controlFreqMultiplier + 1):
            self.mainTank.step(flowrate)
            
        self.iterCount = self.iterCount + 1

        print(" iter: " + str(self.iterCount) + " and hLiq: " + str(self.mainTank.hLiq) + " and hSetPoint: " + str(self.mainTank.hSetPoint))

        if self.iterCount > 150 and (not self.SPChangeDone):
            self.mainTank.hSetPoint = random.randrange(1,4,1)
            self.SPChangeDone = True

class Tanker(Fmi2Slave):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.flowrate = 10.
        self.hSetPoint = 2.
        self.tc = TankController(2, self.flowrate, 800)
        self.hLiq = self.tc.mainTank.hLiq

        self.register_variable(Real("flowrate", causality=Fmi2Causality.input))
        self.register_variable(Real("hLiq", causality=Fmi2Causality.output))
        self.register_variable(Real("hSetPoint", causality=Fmi2Causality.output))

    def do_step(self, current_time, step_size):
        self.tc.step(self.flowrate)
        self.hLiq = self.tc.mainTank.hLiq
        self.hSetPoint = self.tc.mainTank.hSetPoint
        return True
    
