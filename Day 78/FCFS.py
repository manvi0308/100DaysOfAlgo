''' Given n processes with their burst times, the task is to find average waiting time and average turn around time using FCFS scheduling algorithm.
First in, first out (FIFO), also known as first come, first served (FCFS), is the simplest scheduling algorithm. FIFO simply queues processes in the order that they arrive in the ready queue.
In this, the process that comes first will be executed first and next process starts only after the previous gets fully executed.
Here we are considering that arrival time for all processes is 0.

How to compute below times in Round Robin using a program?

Completion Time: Time at which process completes its execution.
Turn Around Time: Time Difference between completion time and arrival time. Turn Around Time = Completion Time – Arrival Time
Waiting Time(W.T): Time Difference between turn around time and burst time.
Waiting Time = Turn Around Time – Burst Time

Implementation:

1-  Input the processes along with their burst time (bt).
2-  Find waiting time (wt) for all processes.
3-  As first process that comes need not to wait so 
    waiting time for process 1 will be 0 i.e. wt[0] = 0.
4-  Find waiting time for all other processes i.e. for
     process i -> 
       wt[i] = bt[i-1] + wt[i-1] .
5-  Find turnaround time = waiting_time + burst_time 
    for all processes.
6-  Find average waiting time = 
                 total_waiting_time / no_of_processes.
7-  Similarly, find average turnaround time = 
                 total_turn_around_time / no_of_processes '''
                 
 # Python3 program for implementation 
# of FCFS scheduling 

# Function to find the waiting 
# time for all processes 
def findWaitingTime(processes, n, 
					bt, wt): 

	# waiting time for 
	# first process is 0 
	wt[0] = 0

	# calculating waiting time 
	for i in range(1, n ): 
		wt[i] = bt[i - 1] + wt[i - 1] 

# Function to calculate turn 
# around time 
def findTurnAroundTime(processes, n, 
					bt, wt, tat): 

	# calculating turnaround 
	# time by adding bt[i] + wt[i] 
	for i in range(n): 
		tat[i] = bt[i] + wt[i] 

# Function to calculate 
# average time 
def findavgTime( processes, n, bt): 

	wt = [0] * n 
	tat = [0] * n 
	total_wt = 0
	total_tat = 0

	# Function to find waiting 
	# time of all processes 
	findWaitingTime(processes, n, bt, wt) 

	# Function to find turn around 
	# time for all processes 
	findTurnAroundTime(processes, n, 
					bt, wt, tat) 

	# Display processes along with all details 
	print( "Processes Burst time " +
				" Waiting time " +
				" Turn around time") 

	# Calculate total waiting time 
	# and total turn around time 
	for i in range(n): 
	
		total_wt = total_wt + wt[i] 
		total_tat = total_tat + tat[i] 
		print(" " + str(i + 1) + "\t\t" +
					str(bt[i]) + "\t " +
					str(wt[i]) + "\t\t " +
					str(tat[i])) 

	print( "Average waiting time = "+
				str(total_wt / n)) 
	print("Average turn around time = "+
					str(total_tat / n)) 


