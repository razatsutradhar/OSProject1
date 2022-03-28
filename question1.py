from alogoritms.FIFO import FIFO
from alogoritms.SJF import SJF
from alogoritms.RR import RR
from process import Process
from process import csv_to_processes

#returns an array of Process objects
array_of_processes = csv_to_processes('data/processes.csv')
# print(array_of_processes)

arr = RR(array_of_processes)
print("\n\n")
print("shortest job first")
SJF(array_of_processes)
print("RR")
print("wait time: " + str(arr[0]))
print("Turn around time " + str(arr[1]))

print(FIFO(array_of_processes))




