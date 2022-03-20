# batchSchedulingComparison.py
# Paige Mortensen
# CS 446 PA2 - compare, contrast, and simulate process management algorithms

# As part of your file header, compare and contrast the three algorithms.
# Be sure to explain where each would be appropriate to use,
# and any possible tradeoffs in implementation or process execution

# shortest job has a greater likelihood of encountering more interrupts
# there might be a more efficient ordering for FCFS

import sys


def avg_turnaround(process_completion_times, process_arrival_times):
    turnaround_times = []
    total = 0
    for elem in range(0, len(process_completion_times)):
        turnaround_time = process_completion_times[elem] - process_arrival_times[elem]          # calc turnaround
        turnaround_times += [turnaround_time]                                                   # add time to list
        total += turnaround_time                                                                # add to turnTotal
    avg_turn_time = total / len(turnaround_times)                                               # calc average
    return [turnaround_times, avg_turn_time]


def avg_wait(process_turnaround_times, process_burst_times):
    wait_total = 0
    for elem in range(0, len(process_turnaround_times)):
        wait_time = process_turnaround_times[elem] - process_burst_times[elem]      # take the difference
        wait_total += wait_time                                                     # add to total
    wait_avg = wait_total / (len(process_turnaround_times))                         # calc average
    return wait_avg


def first_come_first_served_sort(data):
    data.sort(key=lambda x: x[0])                       # sort by PID so edge case is set up
    data.sort(key=lambda x: x[1])                       # sort by arrival time
    completion_list = []
    current_time = 0
    for elem in range(0, len(data)):                    # find completion times
        completion = current_time + data[elem][2]       # completion = currentTime + burstTime
        completion_list += [completion]                 # add to list
        current_time += data[elem][2]                   # new current time
    return [data, completion_list]


def shortest_job_first_sort(data):
    queue = []
    pid_list = []

    data.sort(key=lambda x: x[0])               # sort by PID so edge case is set up
    data.sort(key=lambda x: x[1])               # sort by arrival time - active process should be at front
    for elem in range(0, len(data)):            # load all processes into queue - active process should be at front
        queue.append(data[elem])
    pid_list += [data[0][0]]                    # list first PID

    while not queue == []:                              # while there are still processes waiting to be run,
        print(queue)
        if len(queue) == 1:
            queue.pop(0)
        else:
            for j in range(0, len(queue)-1):                # check that all processes have remaining time
                if queue[j][2] <= 0:                        # if the active process has reached 0 time remaining
                    queue.pop(0)                            # remove from the queue (process finished).
            for index in range(1, len(queue)):              # iterate through the remaining waiting processes.
                if queue[index][2] < queue[0][2]:           # if the next process has a shorter burst than the current
                    queue[0][2] -= queue[index][1]          # decrement the burst of active process by arrival of next
                    queue.insert(0, queue[index])           # place new active process at front
                    queue.pop(index+1)                      # remove process from old location
                    pid_list += [queue[0][0]]               # list new active process
                else:
                    queue[0][2] -= 1                        # otherwise, decrement remaining time of active
    print(queue)

    # if the burst of the newest process in the queue is less than the remaining time to execute the current process,
    # the current process should be added back to the queue and the new process should be executed
    return data


def priority_sort(data):
    data.sort(key=lambda x: x[0])                       # sort by PID
    data.sort(key=lambda x: x[3])                       # sort by priority
    data.sort(key=lambda x: x[1])                       # sort by arrival time
    # completion_list = []
    # current_time = 0
    # for elem in range(0, len(data)):  # find completion times
    #     completion = current_time + data[elem][2]  # completion = currentTime + burstTime
    #     completion_list += [completion]  # add to list
    #     current_time += data[elem][2]  # new current time
    # return [data, completion_list]


def main():
    sorting = {"FCFS", "ShortestFirst", "Priority"}
    pid_list = []
    arrival_time_list = []
    burst_time_list = []
    priority_list = []
    completion_list = []
    data_2d = []

    if len(sys.argv) != 3:                                                                  # check num of arguments
        print("you did not enter the correct number of arguments")
        print("what is the name of your process file?")
        file = input()
        sys.argv[1] = file
        print("what sort type would you like to use?")
        sort = input()
        sys.argv[2] = sort                                                       # ERROR: INDEX 2 DOESN'T EXIST HERE ???

    if not any(ele in sys.argv[2] for ele in sorting):                                      # did you provide a sort
        print("your process scheduling options are FCFS, ShortestFirst, or Priority")
        quit()
    elif not open(sys.argv[1], 'r'):                                                        # does this file exist
        print("your file doesn't exist")
        quit()
    else:                                                                                   # then parse the input
        with open(sys.argv[1], 'r') as f:
            index = 0
            for line in f:
                pid, arrival_time, burst_time, priority = line.split(', ')
                data_list = [int(pid), int(arrival_time), int(burst_time), int(priority)]   # 2D array of all data
                data_2d.insert(index, data_list)
                index += 1

    if sys.argv[2] == "FCFS":                                                               # FCFS
        fcfs_ret = first_come_first_served_sort(data_2d)
        data_2d = fcfs_ret[0]
        completion_list = fcfs_ret[1]
        for elem in range(0, len(data_2d)):
            print(data_2d[elem][0])
        for elem in range(0, 4):
            pid_list += [int(data_2d[elem][0])]                                             # update arrays - sorted
            arrival_time_list += [int(data_2d[elem][1])]
            burst_time_list += [int(data_2d[elem][2])]
            priority_list += [int(data_2d[elem][3])]
        turnaround_ret = avg_turnaround(completion_list, arrival_time_list)                 # calculate times
        turnaround_list = turnaround_ret[0]
        avg_turnaround_time = turnaround_ret[1]
        wait = avg_wait(turnaround_list, burst_time_list)
        print("Average Process Turnaround Time: " + str(avg_turnaround_time))               # print
        print("Average Process Wait Time: " + str(wait))
    elif sys.argv[2] == "ShortestFirst":
        sjf_ret = shortest_job_first_sort(data_2d)
    elif sys.argv[2] == "Priority":
        prio_ret = priority_sort(data_2d)


if __name__ == "__main__":
    main()
