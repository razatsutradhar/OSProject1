import csv


class Process:
    time_completed = -1
    done = False

    def __init__(self, pid, cpu_cycle, mem):
        self.pid = pid
        self.cpu_cycles = cpu_cycle
        self.cycles_left = cpu_cycle
        self.mem = mem

    # enter current time and number of cpu cycles you want to execute
    # will return howmany were acually executed
    # use return value to increment time
    def execute_for(self, c, t):
        if not self.done and self.cycles_left - c <= 0:
            cp = self.cycles_left
            self.time_completed = t + self.cycles_left
            self.cycles_left = 0
            self.done = True
            # print("executed processes " + str(self.pid) + " for " + str(cp) + " cpu cycles and completed")
            return int(cp)
        elif not self.done:
            self.cycles_left -= c
            # print("executed processes " + str(self.pid) + " for " + str(c) + " cpu cycles; " + str(
            #     self.cycles_left) + " cpu cycles left")
            return int(c)
        else:
            return 0

    # string representation of a Process object
    def __repr__(self):
        if self.done:
            return "[PID: " + str(self.pid) + ", Cycles: " + str(self.cpu_cycles) + ", Memory: " + str(
                self.mem) + ", Time Done: " + str(self.time_completed) + "]"
        else:
            return "[PID: " + str(self.pid) + ", Cycles: " + str(self.cpu_cycles) + ", Memory: " + str(self.mem) + "]"


#function to return an array of processes based from a CSV file
def csv_to_processes(path):
    processData = []
    with open(path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        for p in csvreader:
            proc = Process(pid=int(p[0]), cpu_cycle=int(p[1]), mem=int(p[2]))
            processData.append(proc)
    return processData
