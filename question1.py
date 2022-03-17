from alogoritms.FIFO import FIFO
from alogoritms.SJF import SJF
from alogoritms.RR import RR
from process import Process
from process import csv_to_processes

#returns an array of Process objects
array_of_processes = csv_to_processes('data/processes_1.csv')
print(array_of_processes)

print(RR(array_of_processes))

#calculate average awaiting time and average turn around time using SJF
print("\nCalculate awaiting time and average time using SJF")
SJF(6)
