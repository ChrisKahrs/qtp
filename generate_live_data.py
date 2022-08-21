import time
import numpy.random as random

data_file = open("data.txt", "w+")
i = 0
while True:
    val = random.randint(-20, 20)
    with open("data.txt", "a+") as file:
        file.write((str(i) + "," + str(val) + "\n"))
    i += 1
    time.sleep(1)
