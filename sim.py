from tank import Tank

blt = Tank(1, 11)
blt.hSetPoint = 2

for i in range(blt.T):
    blt.step()
    
    if i % 10 == 1:
        print("current time: " + str(i) + " and blt height: " + str(blt.hLiq))
        
    if blt.overflowed:
        print("overflow!!")
        break