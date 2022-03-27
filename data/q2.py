from alogoritms.RR import RR
from process import Process, csv_to_processes
from alogoritms.RR import AllNone

jobs = csv_to_processes('data/processes_1.csv')
jobs.sort(key=lambda x: x.cpu_cycles)

processors = []
finishedList = []

totalCPU = 0
for p in jobs:
    totalCPU += p.cpu_cycles

threshhold = (totalCPU*2)/3
short = []
long = []
shortFinished = []
longFinished = []
littleProcessors = []
bigProcessors = []
totalCPU = 0

for p in jobs:
    if totalCPU < threshhold:
        short.append(p)
        totalCPU += p.cpu_cycles
    else:
        long.append(p)

for i in range(0,3):
    littleProcessors.append(long.pop(0))
    bigProcessors.append(short.pop(0))

t = 0
while len(short)>0 and len(long)>0 and len(bigProcessors)>0 and len(littleProcessors)>0:
    times = []
    for p in littleProcessors:
        if p is not None:
            times.append(p.cycles_left/4)
    for p in bigProcessors:
        if p is not None:
            times.append(p.cycles_left/8)

    print(min(times))
    minTime = min(times)
    print(littleProcessors)
    print(bigProcessors)
    print()
    for p in littleProcessors:
        if p is not None:
            p.execute_for(minTime*4, t*4)
            if p.done:
                finishedList.append(p)
                longFinished.append(p)
                littleProcessors.remove(p)
                if len(long) > 0:
                    littleProcessors.append(long.pop(0))

    for p in bigProcessors:
        if p is not None:
            p.execute_for(minTime*8, t*8)
            if p.done:
                finishedList.append(p)
                shortFinished.append(p)
                bigProcessors.remove(p)
                if len(long) > 0:
                    bigProcessors.append(short.pop(0))

    t+= minTime

waitTime = 0
turnTime = 0
cpuTotal = 0
# print(short)
# print(long)
for p in shortFinished:
    waitTime += (p.time_completed-p.cpu_cycles)/8
    turnTime += p.time_completed/8
    cpuTotal += p.cpu_cycles

for p in longFinished:
    waitTime += (p.time_completed-p.cpu_cycles)/8
    turnTime += p.time_completed/8
    cpuTotal += p.cpu_cycles
# print(finishedList)
# print(cpuTotal)
waitTime /= len(finishedList)
turnTime /= len(finishedList)
# print(jobs)
print("wait: " + str(waitTime))
print("turn around: " + str(turnTime))
