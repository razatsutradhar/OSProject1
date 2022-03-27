from alogoritms.FIFO import FIFO
from alogoritms.SJF import SJF_Q4
from alogoritms.RR import RR
from process import Process
from process import csv_to_processes

#returns an array of Process objects
array_of_processes = csv_to_processes('data/processes_1.csv')

#Question 4 SJF

result = (SJF_Q4(250,array_of_processes))
print("==========Question 4==========")
print("SJF: ")
print("Average waiting time scheduling using SJF is ", (result['waiting_time'] / 250))
print("Average Turnaround Time scheduling using SJF is ", (result['turnaround_time'] / 250))
