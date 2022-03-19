# batchSchedulingComparison.py
# Paige Mortensen
# CS 446 PA2 - compare, contrast, and simulate process management algorithms

# As part of your file header, compare and contrast the two algorithms.
# Be sure to explain where each would be appropriate to use,
# and any possible tradeoffs in implementation or process execution


def main():
    # from terminal: enter the program name, batchfileName, and type of process sort you would like to do
    #   for example: python3 batchSchedulingComparison.py batchfile.txt

    # If the user does not enter your three arguments (program name batchfileName and sortType),
    #   then you should prompt the user repeatedly and take their input until they enter the correct number of arguments
    # Once the user supplies the correct number of arguments
    #   use argv to get the batch file name, and then read all the data from it, if you can
    # If you can't (because the user entered a non-existing file name)
    #   tell the user that the file doesn't exist and exit the program
    # If you're able to read from the file name provided by the user
    #   then you should get the algorithm name from the argv list
    # If the user does not provide one of these arguments
    #   tell the user that their process scheduling options are FCFS, ShortestFirst, or Priority, and exit the program
    # If the user enters an acceptable algorithm name
    #   perform a logical check to see which function you should call

    # For each algorithm, the output to the terminal should be the processes in the order that they should execute,
    # the average process waiting time, and the average process turn around time, each on their own line. All input
    # and output should be gathered and executed IN MAIN

    # Please print to 2 decimal places

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
    