import heapq

class PriorityProcess:
    def __init__(self, pid, burst_time, priority, arrival_time=0):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority # Lower number = Higher priority
        self.arrival_time = arrival_time
        self.completion_time = 0

    # Tie-breaker: Priority first, then Arrival Time
    def __lt__(self, other):
        if self.priority == other.priority:
            return self.arrival_time < other.arrival_time
        return self.priority < other.priority

def priority_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)
    time_elapsed = 0
    pq = []  # Ready queue (Heap)
    unfinished = processes[:]
    completed_processes = []

    print("\nPreemptive Priority Scheduling\n")

    while unfinished or pq:
        # 1. Move arrived processes to the Priority Queue
        while unfinished and unfinished[0].arrival_time <= time_elapsed:
            heapq.heappush(pq, unfinished.pop(0))

        if not pq:
            # CPU Idle
            time_elapsed = unfinished[0].arrival_time
            continue

        # 2. Pick the highest priority process
        current = heapq.heappop(pq)
        
        print(f"[Time {time_elapsed}] P{current.pid} (Pri: {current.priority}) is running")
        
        # 3. Run for 1 unit of time (to check for arrivals/preemption)
        current.remaining_time -= 1
        time_elapsed += 1

        if current.remaining_time == 0:
            current.completion_time = time_elapsed
            print(f"--- P{current.pid} completed at {time_elapsed} ---")
            completed_processes.append(current)
        else:
            # Push back to PQ to re-evaluate priority against any new arrivals
            heapq.heappush(pq, current)

    return completed_processes

# Example
procs = [
    PriorityProcess(pid=1, burst_time=10, priority=2, arrival_time=0),
    PriorityProcess(pid=2, burst_time=1,  priority=1, arrival_time=2) # Will preempt P1
]
priority_scheduling(procs)