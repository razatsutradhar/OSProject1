from alogoritms.RR import RR
from process import Process, csv_to_processes
from alogoritms.RR import AllNone

que = csv_to_processes('data/processes.csv')
jobs = []
processors = []
finishedList = []

totalCPU = 0
short = []
long = []
shortFinished = []
longFinished = []
littleProcessors = []
bigProcessors = []
smallProcessorSpeed = 2*pow(10,9)
bigProcessorSpeed = 4*pow(10,9)
smallMemoryMax = 8000
delay = 1

temp = []

def reorganize(jobs, short, long):
    jobs += short
    jobs += long
    jobs.sort(key=lambda x: x.cpu_cycles)

    totalCPU = 0
    for p in jobs:
        totalCPU += p.cpu_cycles

    threshhold = (totalCPU*2)/3
    short = []
    long = []
    totalCPU = 0
    smallMemoryMax = 8000

    temp = []
    for p in jobs:
        if p.mem > smallMemoryMax:
            short.append(p)
            threshhold -= p.cpu_cycles
        else:
            temp.append(p)
    jobs = temp

    for p in jobs:
        if totalCPU < threshhold:
            short.append(p)
            totalCPU += p.cpu_cycles
        else:
            long.append(p)

    long.sort(key=lambda x: x.cpu_cycles)
    short.sort(key=lambda x: x.cpu_cycles)
    return [jobs, short, long]


for i in range(0,3):
    if len(long) > 0:
        littleProcessors.append(long.pop(0))

    if len(short) > 0:
        bigProcessors.append(short.pop(0))

t = 0
delayTime = delay
while len(short)>0 or len(long)>0 or len(bigProcessors)>0 or len(littleProcessors)>0 or len(que)>0:

    if len(que) > 0:
        times = [delayTime]
    else:
        times = []

    for p in littleProcessors:
        if p is not None:
            times.append(p.cycles_left/smallProcessorSpeed)
    for p in bigProcessors:
        if p is not None:
            times.append(p.cycles_left/bigProcessorSpeed)

    # print(min(times))
    minTime = min(times)
    # print(littleProcessors)
    # print(bigProcessors)
    # print()

    for p in littleProcessors:
        p.execute_for(minTime*smallProcessorSpeed, t*smallProcessorSpeed)
        if p.done:
            p.time_completed = t
            finishedList.append(p)
            longFinished.append(p)
            littleProcessors.remove(p)
            if len(long) > 0:
                littleProcessors.append(long.pop(0))

    for p in bigProcessors:
        if p is not None:
            p.execute_for(minTime*bigProcessorSpeed, t*bigProcessorSpeed)
            if p.done:
                p.time_completed = t
                finishedList.append(p)
                shortFinished.append(p)
                bigProcessors.remove(p)
                if len(short) > 0:
                    bigProcessors.append(short.pop(0))
    delayTime -= minTime

    if delayTime <= 0 and len(que)>0:
        newProcess = que.pop(0)
        # print(newProcess)
        newProcess.enter_queue_time = t
        jobs.append(newProcess)
        newLists = reorganize(jobs, short, long)
        # print(len(jobs))
        jobs = []
        # print(len(jobs))
        short = newLists[1]
        long = newLists[2]
        delayTime = delay

    if len(littleProcessors) < 3 and len(long) > 0:
        addOn = min((3 - len(littleProcessors)), len(long))
        for i in range(0, addOn):
            littleProcessors.append(long.pop(0))

    if len(bigProcessors) < 3 and len(short) > 0:
        addOn = min((3 - len(bigProcessors)), len(short))
        for i in range(0, addOn):
            bigProcessors.append(short.pop(0))
    t+= minTime

waitTime = 0
turnTime = 0
cpuTotal = 0
for p in shortFinished:
    waitTime += (p.time_completed - p.cpu_cycles/bigProcessorSpeed - p.enter_queue_time)
    turnTime += p.time_completed - p.enter_queue_time
    cpuTotal += p.cpu_cycles

for p in longFinished:
    waitTime += (p.time_completed - p.cpu_cycles/smallProcessorSpeed - p.enter_queue_time)
    turnTime += p.time_completed - p.enter_queue_time
    cpuTotal += p.cpu_cycles
# print(finishedList)
# print(cpuTotal)
waitTime /= len(finishedList)
turnTime /= len(finishedList)
print("wait: " + str(waitTime))
print("turn around: " + str(turnTime))