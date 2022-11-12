from tank import Tank

blt = Tank(0.7, 15)
brt = Tank(0.7, 15)
tlt = Tank(0.3, 15)
trt = Tank(0.3, 15)

# find equalibrium height for each tank
           
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