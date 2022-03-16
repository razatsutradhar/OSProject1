
#Linh
#Completion Time: Time at which process completes its execution.
#Turn Around Time: Time Difference between completion time and arrival time. Turn Around Time = Completion Time – Arrival Time
#Waiting Time(W.T): Time Difference between turn around time and burst time. 
#Waiting Time = Turn Around Time – Burst Time

#Burst Time = random(10 * pow(10,6) - 10* pow(10,12))

#turnArroundTime = completionTime - arrangeArrival
#waitingTime = TurnArroundTime - BurstTime


import random
import math

def arrangeArrival(n, array):
    for i in range(0, n):
        for j in range(i, n-i-1):
            if array[1][j] > array[1][j+1]:
                for k in range(0, n):
                    array[k][j], array[k][j+1] = array[k][j+1], array[k][j]
  
  
def CompletionTime(n, array):
    value = 0
    array[3][0] = array[1][0] + array[2][0]
    array[5][0] = array[3][0] - array[1][0]
    array[4][0] = array[5][0] - array[2][0]
    for i in range(1, n):
        temp = array[3][i-1]
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
  
  
if __name__ == '__main__':

    # n is number of processors (6)
    n = 6

  
#procress id: arr[0] in range (1,6)

#burst time: arr[2] in range from 0 to random(10 * pow(10,6) - 10* pow(10,12))

#arrival time: arr[1] in range from 1 to 250

    x = (10*math.pow(10,12) - 10*math.pow(10,6))
    

    #initialize 2 dimenssion array to compute the arrangeArrival and Completion Time
    #time[0], time[1], time[2], time[4], time[5] will represent for value of process id , arrival time, burst time,
    #waiting time, turn around time
    time = [[int(i) for i in range(1, n+1)], [0]*n,
           [0]*n, [0]*n, [0]*n, [0]*n]

    for i in range(0,n):
        time[1][i] = random.randint(1,256)
        time[2][i] = random.randint(1,x)
        
    arrangeArrival(n, time)
    CompletionTime(n, time)
    waitingtime = 0
    turaroundtime = 0
    for i in range(0, n):
        waitingtime += time[4][i]
        turaroundtime += time[5][i]
    print("Average waiting time scheduling using SJF is ", (waitingtime/n))
    print("Average Turnaround Time scheduling using SJF is  ", (turaroundtime/n))
  
