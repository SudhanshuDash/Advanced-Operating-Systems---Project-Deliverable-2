def calculate_metrics(processes):
    print("\nPerformance Metrics")
    print("-" * 65)
    print(f"{'PID':<5} | {'Wait Time':<12} | {'Turnaround':<12} | {'Response':<10}")
    print("-" * 65)

    total_waiting_time = 0
    total_turnaround_time = 0
    count = len(processes)

    for p in processes:
        # Turnaround Time = Completion Time - Arrival Time
        turnaround = p.completion_time - p.arrival_time
        
        # Waiting Time = Turnaround Time - Burst Time
        waiting = turnaround - p.burst_time
        
        # Response Time = First Start Time - Arrival Time
        # We use a fallback of 0 if start_time wasn't set, though it should be.
        response = (p.start_time - p.arrival_time) if p.start_time is not None else 0

        # Accumulate totals for averages
        total_waiting_time += waiting
        total_turnaround_time += turnaround

        print(
            f"P{p.pid:<4} | {waiting:<12} | {turnaround:<12} | {response:<10}"
        )

    if count > 0:
        print("-" * 65)
        print(f"Average Waiting Time:    {total_waiting_time / count:.2f}")
        print(f"Average Turnaround Time: {total_turnaround_time / count:.2f}")
    print("-" * 65)