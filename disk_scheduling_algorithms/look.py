def look(disk_queue, head_start, direction='up'):
    """
    LOOK disk scheduling algorithm.
    Parameters:
        disk_queue: list of requests.
        head_start: initial position of the disk head.
        direction: initial direction of head movement ('up' or 'down').
    Returns:
        total_seek_count: total head movements to serve all requests.
        seek_sequence: the sequence in which requests are served.
    """
    seek_sequence = []
    total_seek_count = 0
    current_head = head_start
    up_sequence = sorted([r for r in disk_queue if r >= current_head])
    down_sequence = sorted([r for r in disk_queue if r < current_head], reverse=True)

    if direction == 'up':
        for request in up_sequence:
            total_seek_count += abs(current_head - request)
            seek_sequence.append(request)
            current_head = request

        for request in down_sequence:
            total_seek_count += abs(current_head - request)
            seek_sequence.append(request)
            current_head = request

    elif direction == 'down':
        for request in down_sequence:
            total_seek_count += abs(current_head - request)
            seek_sequence.append(request)
            current_head = request

        for request in up_sequence:
            total_seek_count += abs(current_head - request)
            seek_sequence.append(request)
            current_head = request

    return total_seek_count, seek_sequence
