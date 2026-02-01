from collections import deque

class Process:
    def __init__(self, pid, burst_time, arrival_time=0):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.arrival_time = arrival_time
        self.completion_time = 0

def round_robin(processes, quantum):
    # 1. Sort processes by arrival time initially
    processes.sort(key=lambda x: x.arrival_time)
    
    time_elapsed = 0
    ready_queue = deque()
    unfinished_processes = processes[:]
    completed_processes = []

    print(f"\nRound-Robin Scheduling (Quantum = {quantum})\n")

    # Keep running until all processes are done
    while unfinished_processes or ready_queue:
        
        # 2. Add all processes that have arrived by now to the ready queue
        arrived = [p for p in unfinished_processes if p.arrival_time <= time_elapsed]
        for p in arrived:
            ready_queue.append(p)
            unfinished_processes.remove(p)

        if not ready_queue:
            # CPU is idle; jump to the arrival time of the next process
            time_elapsed = unfinished_processes[0].arrival_time
            continue

        process = ready_queue.popleft()
        run_time = min(quantum, process.remaining_time)
        
        print(f"[Time {time_elapsed}] P{process.pid} runs for {run_time} units")
        
        time_elapsed += run_time
        process.remaining_time -= run_time

        # 3. Check for new arrivals DURING the time this process was running
        # This is critical for Round-Robin!
        newly_arrived = [p for p in unfinished_processes if p.arrival_time <= time_elapsed]
        for p in newly_arrived:
            ready_queue.append(p)
            unfinished_processes.remove(p)

        if process.remaining_time > 0:
            # Re-add the current process to the back of the queue
            ready_queue.append(process)
        else:
            process.completion_time = time_elapsed
            completed_processes.append(process)
            print(f"--- P{process.pid} completed at {time_elapsed} ---")

    return completed_processes

# Example Usage:
procs = [Process(1, 10, 0), Process(2, 4, 2), Process(3, 5, 4)]
round_robin(procs, 3)
