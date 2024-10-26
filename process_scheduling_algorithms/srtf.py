def srtf(processes):
    """
    Shortest Remaining Time First (Preemptive SJF) Scheduling Algorithm.
    Parameters:
        processes: List of tuples (process_id, arrival_time, burst_time).
    Returns:
        waiting_times, turnaround_times: Lists of waiting and turnaround times for each process.
    """
    n = len(processes)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    burst_remaining = [p[2] for p in processes]
    current_time = 0
    completed = 0
    last_process = -1

    while completed < n:
        # Find process with shortest remaining burst time
        available_processes = [
            i for i in range(n) if processes[i][1] <= current_time and burst_remaining[i] > 0
        ]
        if available_processes:
            idx = min(available_processes, key=lambda x: burst_remaining[x])
            burst_remaining[idx] -= 1

            if burst_remaining[idx] == 0:
                completed += 1
                turnaround_times[idx] = current_time - processes[idx][1] + 1
                waiting_times[idx] = turnaround_times[idx] - processes[idx][2]

            last_process = idx
        current_time += 1

    return waiting_times, turnaround_times
