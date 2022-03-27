
#Julian
def FIFO(array_of_processes, n):
     # sort the array of processes ascending by arrival time
    array_of_processes.sort(key=lambda array_of_processes:(array_of_processes[1]))
    print(array_of_processes)

def calc_waiting_time(array_of_processes, n):
    
 


    # loop through the processes starting from the second process as the first one has 0 waiting time
    # Calculate the waiting time of each process
    # If arrival time of the process is greater than the sum of arrival and burst time of the pervious process in the queue
    # then the process didn't wait in the queue and waiting time equals 0
    
    
    # Waiting Time for the first process
     array_of_processes[0].append('0')
    
    # The loop to calculate and append each process waiting time
     for i in range (1,n):
          if array_of_processes[i][1] > array_of_processes[i-1][2]+array_of_processes[i-1][1]:
            waiting_time = 0
          else:        
            waiting_time = array_of_processes[i-1][2]+array_of_processes[i-1][1]-array_of_processes[i][1]
          array_of_processes[i].append(waiting_time)
        
def calc_turn_around_time(array_of_processes, n):
    
    
    # Turn Around Time for the first process
    array_of_processes[0].append('0')
    
    # The loop to calculate and append each process waiting time
    for i in range (1,n):
        if array_of_processes[i][1] > array_of_processes[1][2]+array_of_processes[1][1]:
            Turn_Around_time = 0
        
    
    # Print the table of the processes:
    print('Process_ID\tArrival_Time\tBurst_Time\tWaiting_Time\tTurn_Around_Time')
    for i in range(n):
        print(array_of_processes[i][0],'\t\t',array_of_processes[i][1],'\t\t',array_of_processes[i][2],'\t\t',array_of_processes[i][3],'\t\t',array_of_processes[i][4])
    
    #return the new array processes with calculated waiting time
    return array_of_processes
    
def calc_total_waiting_time(new_array_of_processes, n):
    
    # Initiate a variable for the total waiting time
    total_waiting_time = 0
    
    # Summition of the total waiting times to calculate the total
    for i in range(1,n):
        total_waiting_time += new_array_of_processes[i][3]
    
    # Return total waiting time
    return total_waiting_time
    

def calc_avg_waiting_time(total_waiting_time, n):
    
    #calculate average waiting time and print it
    avg_waiting_time = total_waiting_time / n
    print('The Average Waiting Time: {}'.format(avg_waiting_time))
    
    
def calc_total_turn_around_time(new_array_of_processes, n):
    
    # Initiate a variable for the total turn around time
    total_turn_around_time = 0
    
    # Summition of the total turn around times to calculate the total
    for i in range(1,n):
        total_turn_around_time += new_array_of_processes[i][4]
    
    # Return total turn around time
    return total_turn_around_time
    
def calc_avg_turn_around_time(total_turn_around_time, n):
    
    #calculate average turn around time and print it
    avg_turn_around_time = total_turn_around_time / n
    print('The Average Turn Around Time: {}'.format(avg_turn_around_time))