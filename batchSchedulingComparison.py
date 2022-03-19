# batchSchedulingComparison.py
# Paige Mortensen
# CS 446 PA2 - compare, contrast, and simulate process management algorithms

# As part of your file header, compare and contrast the two algorithms.
# Be sure to explain where each would be appropriate to use,
# and any possible tradeoffs in implementation or process execution

import sys
from DistUpgrade.DistUpgradeViewText import readline


def avg_turnaround():
    # Turnaround time is calculated by subtracting each processCompletionTime from its arrivalTime
    #   For example, using FCFS (see below) process 3 takes 50 seconds to execute and arrived at time 0,
    #   so process 3 has a turnaround time of 70 because it has to wait 20 seconds for process 1 to fully execute
    # To calculate the average, sum each process' turnaround time, and divide by the number of processes
    #   So if we only executed process 1 and 3, we would add 20 and 70 and divide by 2- the turnaround time of those
    #   two processes averaged (ignoring the rest of the list for simplicity) is 45
    return


def avg_wait():
    # Wait time is calculated by subtracting each processBurstTime from its processTurnaroundTime
    #   For example, using FCFS (see below) we previously calculated that process 3 has a turnaround time of 70, and
    #   process 1 has a turnaround time of 20. To calculate the waitTime for process 3, we subtract the burst time
    #   from the turnaround (70-50) and get 20; doing the same for process 1, we get 0
    # To calculate the average, sum each process' wait time, and divide by the number of processes
    #   So if we only executed process 1 and 3, we would add 20 and 0 and divide by 2
    #   the wait time of those two processes averaged (ignoring the rest of the list for simplicity) is 10
    return


def first_come_first_served_sort():
    #
    return


def shortest_job_first_sort():
    #
    return


def priority_sort():
    #
    return


def main(argv):
    sorting = {"FCFS", "ShortestFirst", "Priority"}

    if len(sys.argv) != 3:
        print("you did not enter the correct number of arguments")
        print("what is the name of your process file?")
        file = input()
        sys.argv[1] = file
        print("what sort type would you like to use?")
        sort = input()
        sys.argv[2] = sort

    if not open(sys.argv[1], 'r'):                                                      # does this file exist
        print("your file doesn't exist")
        quit()
    else:                                                                               # then parse the input
        with open(sys.argv[1], 'r') as f:
            for line in f:
                print(line)
                pid, arrival_time, burst_time, priority = line.split()

    if not any(ele in sys.argv[2] for ele in sorting):                                  # did you provide a sort
        print("your process scheduling options are FCFS, ShortestFirst, or Priority")
        quit()

    if sys.argv[2] == "FCFS":                                                           # call sorting and print
        first_come_first_served_sort()
    elif sys.argv[2] == "ShortestFirst":
        shortest_job_first_sort()
    elif sys.argv[2] == "Priority":
        priority_sort()
    # For each algorithm, the output to the terminal should be the processes in the order that they should execute,
    # the average process waiting time, and the average process turn around time, each on their own line. All input
    # and output should be gathered and executed IN MAIN
    # Please print to 2 decimal places


if __name__ == "__main__":
    main(sys.argv[1:])

# print("start test")
# print(len(sys.argv))
# print(str(sys.argv))
# print("end test")
