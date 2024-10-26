def round_robin(processes, quantum):
    """
    Round Robin Scheduling Algorithm.
    Parameters:
        processes: List of tuples (process_id, arrival_time, burst_time).
        quantum: Time quantum for each process.
    Returns:
        waiting_times, turnaround_times: Lists of waiting and turnaround times for each process.
    """
    n = len(processes)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    burst_remaining = [p[2] for p in processes]
    time = 0
    queue = []

    # Add processes to queue based on arrival time
    i = 0
    while i < n or queue:
        while i < n and processes[i][1] <= time:
            queue.append(i)
            i += 1

        if queue:
            idx = queue.pop(0)
            served_time = min(burst_remaining[idx], quantum)
            burst_remaining[idx] -= served_time
            time += served_time

            if burst_remaining[idx] == 0:
                turnaround_times[idx] = time - processes[idx][1]
                waiting_times[idx] = turnaround_times[idx] - processes[idx][2]
            else:
                queue.append(idx)  # Re-add to queue if not completed
        else:
            time += 1  # If no process is available, advance time

    return waiting_times, turnaround_times
