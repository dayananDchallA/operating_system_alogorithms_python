def priority_scheduling(processes):
    """
    Priority Scheduling (Non-Preemptive) Algorithm.
    Parameters:
        processes: List of tuples (process_id, arrival_time, burst_time, priority).
    Returns:
        waiting_times, turnaround_times: Lists of waiting and turnaround times for each process.
    """
    processes = sorted(processes, key=lambda x: (x[1], x[3]))  # Sort by arrival and priority
    n = len(processes)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    completion_time = 0
    processed = [False] * n

    for _ in range(n):
        available_processes = [
            i for i in range(n) if not processed[i] and processes[i][1] <= completion_time
        ]
        if available_processes:
            idx = min(available_processes, key=lambda x: processes[x][3])
        else:
            idx = min(range(n), key=lambda x: (processed[x], processes[x][1]))
            completion_time = processes[idx][1]

        processed[idx] = True
        waiting_times[idx] = max(0, completion_time - processes[idx][1])
        completion_time += processes[idx][2]
        turnaround_times[idx] = waiting_times[idx] + processes[idx][2]

    return waiting_times, turnaround_times
