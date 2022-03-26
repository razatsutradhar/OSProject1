
#Linh
#Question 1 SJF
#Sort all processes base on burst time and print out FIFO

import random
import math
def SJF(array_of_processes):
    array_of_processes.sort(key=lambda x: x.cpu_cycles);
    print(array_of_processes)

#Question 4 will sort all processes base on arrival time

#assume 250 process is divided into 6 processor, here we will create a list of processor

#turnArroundTime = completionTime - arrangeArrival
#total number of cycles equals 3*2ghz + 3*4ghz = 18ghz

#calculate total completionTime

#create a 2 dimession array of 250 process
#each process has process id , arrival time, burst time,waiting time, turn around time

#arrival time will be a radom value genrerate from 1 - 10000

import random

#arrangeArrival and Completion Time functions are refer from GeekforGreek with some modification.

def arrangeArrival(n, array):
    for i in range(0, n):
        for j in range(i, n - i - 1):
            if array[1][j] > array[1][j + 1]:
                for k in range(0, 6):
                    array[k][j], array[k][j + 1] = array[k][j + 1], array[k][j]


def CompletionTime(n, array):
    value = 0
    array[3][0] = array[1][0] + array[2][0]
    array[5][0] = array[3][0] - array[1][0]
    array[4][0] = array[5][0] - array[2][0]
    for i in range(1, n):
        temp = array[3][i - 1]
        mini = array[2][i]
        for j in range(i, n):
            if temp >= array[1][j] and mini >= array[2][j]:
                mini = array[2][j]
                value = j
        array[3][value] = temp + array[2][value]
        array[5][value] = array[3][value] - array[1][value]
        array[4][value] = array[5][value] - array[2][value]
        for k in range(0, 6):
            array[k][value], array[k][i] = array[k][i], array[k][value]

# n is number of processors
# array_of_process is array of processes which are from csv file
def SJF_Q4(n, array_of_processes):

    # initialize 2 dimenssion array to compute the arrangeArrival and Completion Time
    # processes[0], processes[1], processes[2], processes[4], processes[5] will represent for value of process id , arrival time, burst time,
    # waiting time, turn around time
    processes = [[0]*n, [0]*n, [0]*n, [0]*n, [0]*n, [0]*n]
    for i in range(1, n):
        processes[0][i] = array_of_processes[i].pid;
        processes[1][i] = random.randint(1,10000);
        processes[2][i] = array_of_processes[i].cpu_cycles;

    arrangeArrival(n, processes)
    CompletionTime(n, processes)
    waitingtime = 0
    turaroundtime = 0
    for i in range(0, n):
        waitingtime += processes[4][i]
        turaroundtime += processes[5][i]
    print("Average waiting time scheduling using SJF is ", (waitingtime / n))
    print("Average Turnaround Time scheduling using SJF is  ", (turaroundtime / n))


