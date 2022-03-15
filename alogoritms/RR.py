#Razat
def RR(jobs):
    t = 0
    # youi can use the function below to sort based on a class attribute
    # jobs.sort(key=lambda x: x.cpu_cycles)
    while True:
        allDone = True
        for p in jobs:
            t = t + p.execute_for(500, t)
            if not p.done:
                allDone = False

        if allDone:
            break

    for p in jobs:
        print("process " + str(p.pid) + " completed at time " + str(p.time_completed))
    return jobs