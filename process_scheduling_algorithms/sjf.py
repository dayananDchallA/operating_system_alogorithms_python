def sjf(processes):
    """
    Shortest Job First (Non-Preemptive) Scheduling Algorithm.
    Parameters:
        processes: List of tuples (process_id, arrival_time, burst_time).
    Returns:
        waiting_times, turnaround_times: Lists of waiting and turnaround times for each process.
    """
    processes = sorted(processes, key=lambda x: (x[1], x[2]))  # Sort by arrival then burst time
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
            # Get the process with the smallest burst time
            idx = min(available_processes, key=lambda x: processes[x][2])
        else:
            idx = min(range(n), key=lambda x: (processed[x], processes[x][1]))
            completion_time = processes[idx][1]

        pid, arrival, burst = processes[idx]
        processed[idx] = True
        waiting_times[idx] = max(0, completion_time - arrival)
        completion_time += burst
        turnaround_times[idx] = waiting_times[idx] + burst

    return waiting_times, turnaround_times
