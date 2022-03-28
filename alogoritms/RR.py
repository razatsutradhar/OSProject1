#Razat
def AllNone(arr):
    for p in arr:
        if p != None:
            return False
    return True
def RR(j):
    jobs = j.copy()
    # youi can use the function below to sort based on a class attribute
    # jobs.sort(key=lambda x: x.cpu_cycles)
    t = 0
    numOfCPUs = 6
    quantum = pow(10,9)
    allDone = True
    slice = quantum
    processors = []
    finishedList = []
    if len(jobs) >= 6:
        for i in range(0,numOfCPUs):
            processors.append(jobs.pop(0))

    elif len(jobs) == 0:
        print("no processes")

    else:
        for i in range(0,len(jobs)):
            processors.append(jobs.pop(0))

    timeSlots = [quantum]*numOfCPUs
    while len(jobs) > 0 or not AllNone(processors):
        # print(str(((1-len(jobs)/250)*100))+ "%")
        times = []
        for i in range(0,numOfCPUs):
            if processors[i] != None:
                # print(processors[i])
                times.append(processors[i].calc_execution_time(timeSlots[i]))
        minTime = min(times)
        t += minTime

        for i in range(0,numOfCPUs):
            # print(processors[i])
            if processors[i] != None:
                processors[i].execute_for(minTime, t)
                # print(processors[i])
                timeSlots[i] -= minTime
                if processors[i].done:
                    finishedList.append(processors[i])
                    timeSlots[i] = quantum
                    if len(jobs) > 0:
                        processors[i] = jobs.pop(0)
                    else:
                        processors[i] = None
                elif timeSlots[i] <= 0:
                    jobs.append(processors[i])
                    timeSlots[i] = quantum
                    if len(jobs) > 0:
                        processors[i] = jobs.pop(0)
                    else:
                        processors[i] = None
        # print("time: " +str(t) )

    waitTime = 0
    turnTime = 0
    cpuTotal = 0
    # print("finished list")
    # print(finishedList)

    # print("jobs")
    # print(jobs)
    for p in finishedList:
        waitTime += (p.time_completed-p.cpu_cycles)
        turnTime += p.time_completed
        cpuTotal += p.cpu_cycles
    # print(finishedList)
    # print(cpuTotal)
    waitTime /= len(finishedList)
    turnTime /= len(finishedList)
    return [waitTime/(2*pow(10, 9)), turnTime/(2*pow(10, 9))]


