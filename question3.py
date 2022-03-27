
#with PA = PB = PC = 2 GHz, and PD = PE = PF = 4GHz
#total cyccles we can use in the CPU at one is 3*2ghz + 3*4ghz = 18ghz
#In general, turnaround time is minimized if most processes finish their next cpu burst within one time quantum.


from alogoritms.FIFO import FIFO
from alogoritms.SJF import SJF
from alogoritms.RR import RR
from process import Process
from process import csv_to_processes

#returns an array of Process objects

import math

array_of_processes = csv_to_processes('data/processes_1.csv')

array_of_processes_memory = []

total_memory_process = 0;
for i in range(0, 250):
    array_of_processes_memory.append(array_of_processes[i].mem);

    #to minimize the turn around time of 250 process, we need to place each process appropriate in to each processor parralel.
    #once it reach capacity of one processor memory it will stop process on that and continute on other one

cpu1_memory = 8*math.pow(10,9)
cpu2_memory = 16*math.pow(10,9)
processor_a = []
total_memory_a = 0
processor_b = []
total_memory_b = 0
processor_c = []
total_memory_c = 0
processor_d = []
total_memory_d = 0
processor_e = []
total_memory_e = 0
processor_f = []
total_memory_f = 0
total_turn_around_time = 0;

for i in range(0, round(250/6)):
    if(total_memory_a < cpu1_memory):
        processor_a.append(array_of_processes_memory[i]);
        total_memory_a += array_of_processes_memory[i];
    if (total_memory_b < cpu1_memory):
        processor_b.append(array_of_processes_memory[i+1]);
        total_memory_b += array_of_processes_memory[i + 1];
    if (total_memory_c < cpu1_memory):
        processor_c.append(array_of_processes_memory[i + 2]);
        total_memory_c += array_of_processes_memory[i + 2];
    if (total_memory_d < cpu2_memory):
        processor_d.append(array_of_processes_memory[i + 3]);
        total_memory_d += array_of_processes_memory[i + 3];
    if (total_memory_e < cpu2_memory):
        processor_e.append(array_of_processes_memory[i + 4]);
        total_memory_e += array_of_processes_memory[i + 4];
    if (total_memory_f < cpu2_memory):
        processor_f.append(array_of_processes_memory[i + 5]);
        total_memory_f += array_of_processes_memory[i + 5];

print("==========Question 3==========")

print("process distributed in process a: ", processor_a)
print("process distributed in process b: ",  processor_b)
print("process distributed in process c: ", processor_c)
print("process distributed in process d: ", processor_d)
print("process distributed in process e: ", processor_e)
print("process distributed in process f: ", processor_f)
