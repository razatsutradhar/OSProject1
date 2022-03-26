#Linh
#Sort all processes base on burst time and print out FIFO
import random
import math
def SJF(array_of_processes):
    array_of_processes.sort(key=lambda x: x.cpu_cycles);
    print(array_of_processes)

#Question 4 will sort all processes base on arrival time

def SJF_Q4(array_of_processes):
    array_of_processes.sort(key=lambda x: x.time_completed);
    print(array_of_processes)