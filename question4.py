from alogoritms.SJF import SJF_Q4
from process import csv_to_processes

#returns an array of Process objects
array_of_processes = csv_to_processes('data/processes_1.csv')

#Question 4 SJF
(SJF_Q4(array_of_processes))
