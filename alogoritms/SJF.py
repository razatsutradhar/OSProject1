
#Linh
#Question 1 SJF
#Sort all processes base on burst time and print out FIFO

import random
import math
def SJF(array_of_processes):
    array_of_processes.sort(key=lambda x: x.cpu_cycles);
    print(array_of_processes)

