# CPU Scheduling Algorithms in Python
A collection of CPU scheduling simulations implemented in Python, including **Round-Robin**, **Preemptive Priority**, and automated **Performance Metric** calculations.
## Features
* **Round-Robin (RR):** Implements time-quantum based scheduling with dynamic arrival handling.
* **Preemptive Priority:** Uses a min-priority heap to handle process preemption when higher-priority tasks arrive.
* **Metrics Suite:** Automatically calculates:
    * **Waiting Time**: Total time a process spends in the ready queue.
    * **Turnaround Time**: Total time from arrival to completion.
    * **Response Time**: Time from arrival until the first time the CPU is allocated.
## Logic & Formulas
The performance metrics are calculated using the following standard operating system formulas:
* **Turnaround Time ($TAT$):** $$TAT = Completion\ Time - Arrival\ Time$$
* **Waiting Time ($WT$):** $$WT = Turnaround\ Time - Burst\ Time$$
* **Response Time ($RT$):** $$RT = First\ Start\ Time - Arrival\ Time$$

