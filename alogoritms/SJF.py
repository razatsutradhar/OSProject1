
#Linh
#Question 1 SJF
#Sort all processes base on burst time and print out FIFO

import random
import math
def SJF(jobs):
    jobs.sort(key=lambda x: x.cpu_cycles)
    print(jobs)
    smallProcessorSpeed = 2 * pow(10, 9)
    t = 0

    for p in jobs:
        # print(p.cpu_cycles/smallProcessorSpeed)
        t += p.cpu_cycles/smallProcessorSpeed
        p.execute_for(p.cpu_cycles, t)
        p.time_completed = t

    waitTime = 0
    turnTime = 0

    for p in jobs:
        waitTime += (p.time_completed - p.cpu_cycles / smallProcessorSpeed - p.enter_queue_time)
        turnTime += p.time_completed - p.enter_queue_time

    waitTime /= len(jobs)
    turnTime /= len(jobs)
    # print(jobs)
    print("wait: " + str(waitTime))
    print("turn around: " + str(turnTime))

    # print(array_of_processes)

