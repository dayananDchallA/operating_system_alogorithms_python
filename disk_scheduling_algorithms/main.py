from disk_scheduling_algorithms.fcfs import fcfs
from disk_scheduling_algorithms.sstf import sstf
from disk_scheduling_algorithms.scan import scan
from disk_scheduling_algorithms.cscan import cscan
from disk_scheduling_algorithms.look import look

def test_disk_scheduling():
    disk_queue = [98, 183, 37, 122, 14, 124, 65, 67]
    head_start = 53
    disk_size = 200

    print("FCFS:", fcfs(disk_queue, head_start))
    print("SSTF:", sstf(disk_queue, head_start))
    print("SCAN (up):", scan(disk_queue, head_start, direction='up', disk_size=disk_size))
    print("C-SCAN:", cscan(disk_queue, head_start, disk_size=disk_size))
    print("LOOK (up):", look(disk_queue, head_start, direction='up'))

test_disk_scheduling()
