def sstf(disk_queue, head_start):
    """
    Shortest Seek Time First (SSTF) disk scheduling algorithm
    Parameters:
        disk_queue: list of requests.
        head_start: initial position of the disk head.
    Returns:
        total_seek_count: total head movements to serve all requests.
        seek_sequence: the sequence in which requests are served.
    """
    seek_sequence = []
    total_seek_count = 0
    current_head = head_start
    requests = disk_queue.copy()

    while requests:
        # Find the request with minimum seek time from current head
        closest_request = min(requests, key=lambda x: abs(current_head - x))
        distance = abs(current_head - closest_request)
        total_seek_count += distance
        seek_sequence.append(closest_request)
        current_head = closest_request
        requests.remove(closest_request)

    return total_seek_count, seek_sequence
