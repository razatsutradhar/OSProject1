from alogoritms.FIFO import FIFO
from alogoritms.SJF import SJF
from alogoritms.RR import RR
from process import Process
from process import csv_to_processes

#returns an array of Process objects
array_of_processes = csv_to_processes('data/processes.csv')
# print(array_of_processes)

print(RR(array_of_processes))

#Question 1 SJF
# (SJF(array_of_processes))
