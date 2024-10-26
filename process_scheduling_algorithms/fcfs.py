def fcfs(processes):
    """
    First-Come, First-Serve Scheduling Algorithm.
    Parameters:
        processes: List of tuples, where each tuple is (process_id, arrival_time, burst_time).
    Returns:
        waiting_times, turnaround_times: Lists of waiting and turnaround times for each process.
    """
    n = len(processes)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    completion_time = 0

    for i, (pid, arrival, burst) in enumerate(processes):
        # Wait time for each process
        waiting_times[i] = max(0, completion_time - arrival)
        # Completion time for current process
        completion_time = max(completion_time, arrival) + burst
        # Turnaround time = waiting time + burst time
        turnaround_times[i] = waiting_times[i] + burst

    return waiting_times, turnaround_times
