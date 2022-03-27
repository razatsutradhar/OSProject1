
#with PA = PB = PC = 2 GHz, and PD = PE = PF = 4GHz
#total cyccles we can use in the CPU at one is 3*2ghz + 3*4ghz = 18ghz
#In general, turnaround time is minimized if most processes finish their next cpu burst within one time quantum.


from alogoritms.FIFO import FIFO
from alogoritms.SJF import SJF_Q4
from alogoritms.RR import RR
from process import Process
from process import csv_to_processes

#returns an array of Process objects

import math

#Question 2 SJF
array_of_processes = csv_to_processes('data/processes_1.csv')

result = (SJF_Q4(250, array_of_processes));

    #to minimize the turn around time of 250 process, we need to place each process appropriate in to each processor parralel.
    #once it reach capacity of one processor it will stop process on that and continute on other one

cpu1_performance = 2*math.pow(10,9)
cpu2_performance = 4*math.pow(10,9)
processor_a = []
total_turn_around_time_processor_a = 0
processor_b = []
total_turn_around_time_processor_b = 0
processor_c = []
total_turn_around_time_processor_c = 0
processor_d = []
total_turn_around_time_processor_d = 0
processor_e = []
total_turn_around_time_processor_e = 0
processor_f = []
total_turn_around_time_processor_f = 0
total_turn_around_time = 0;

for i in range(0,round(len(result['turnaround_time_list'])/6), 6):
    if(total_turn_around_time_processor_a < cpu1_performance):
        processor_a.append(result['turnaround_time_list'][i]);
        total_turn_around_time_processor_a += result['turnaround_time_list'][i];
    if (total_turn_around_time_processor_b < cpu1_performance):
        processor_b.append(result['turnaround_time_list'][i+1]);
        total_turn_around_time_processor_b += result['turnaround_time_list'][i + 1];
    if (total_turn_around_time_processor_c < cpu1_performance):
        processor_c.append(result['turnaround_time_list'][i + 2]);
        total_turn_around_time_processor_c += result['turnaround_time_list'][i + 2];
    if (total_turn_around_time_processor_d < cpu2_performance):
        processor_d.append(result['turnaround_time_list'][i + 3]);
        total_turn_around_time_processor_d += result['turnaround_time_list'][i + 3];
    if (total_turn_around_time_processor_e < cpu2_performance):
        processor_e.append(result['turnaround_time_list'][i + 4]);
        total_turn_around_time_processor_e += result['turnaround_time_list'][i + 4];
    if (total_turn_around_time_processor_f < cpu2_performance):
        processor_f.append(result['turnaround_time_list'][i + 5]);
        total_turn_around_time_processor_f += result['turnaround_time_list'][i + 5];

print("==========Question 2==========")

print("process distributed in process a: ", processor_a)
print("process distributed in process b: ",  processor_b)
print("process distributed in process c: ", processor_c)
print("process distributed in process d: ", processor_d)
print("process distributed in process e: ", processor_e)
print("process distributed in process f: ", processor_f)
