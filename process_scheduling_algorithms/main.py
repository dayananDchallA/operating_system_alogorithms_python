from process_scheduling_algorithms.fcfs import fcfs
from process_scheduling_algorithms.sjf import sjf
from process_scheduling_algorithms.srtf import srtf
from process_scheduling_algorithms.round_robin import round_robin
from process_scheduling_algorithms.priority_scheduling import priority_scheduling

def test_scheduling_algorithms():
    processes = [(1, 0, 8), (2, 1, 4), (3, 2, 9), (4, 3, 5)]  # (process_id, arrival_time, burst_time)
    processes_priority = [(1, 0, 10, 3), (2, 2, 1, 1), (3, 1, 2, 4), (4, 3, 1, 5)]  # (process_id, arrival_time, burst_time, priority)
    quantum = 3

    print("FCFS:", fcfs(processes))
    print("SJF:", sjf(processes))
    print("SRTF:", srtf(processes))
    print("Round Robin:", round_robin(processes, quantum))
    print("Priority Scheduling:", priority_scheduling(processes_priority))
test_scheduling_algorithms()
