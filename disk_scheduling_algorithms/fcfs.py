def fcfs(disk_queue, head_start):
    """
    First-Come, First-Serve (FCFS) disk scheduling algorithm
    Parameters:
        disk_queue: list of requests in the order they arrive.
        head_start: initial position of the disk head.
    Returns:
        total_seek_count: total head movements to serve all requests.
        seek_sequence: the sequence in which requests are served.
    """
    seek_sequence = []
    total_seek_count = 0
    current_head = head_start

    for request in disk_queue:
        # Calculate the distance from current head to the request position
        distance = abs(current_head - request)
        total_seek_count += distance
        seek_sequence.append(request)
        current_head = request  # Move head to the current request position

    return total_seek_count, seek_sequence
