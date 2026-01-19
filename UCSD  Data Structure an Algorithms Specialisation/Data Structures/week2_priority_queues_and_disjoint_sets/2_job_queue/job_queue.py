# python3

from collections import namedtuple
import heapq 

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

def fast_assign(n_workers, jobs):
    result = []
    # Initialize a heap with threads (end_time, thread_index)
    heap = [(0, i) for i in range(n_workers)]  # All threads are free at time 0

    for job in jobs:
        # Get the next available thread
        end_time, thread_index = heapq.heappop(heap)

        # Assign the job to this thread
        result.append(AssignedJob(thread_index, end_time))

        # Update the thread's availability and push it back into the heap
        heapq.heappush(heap, (end_time + job, thread_index))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = fast_assign(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
    
    # with open(r"C:\Users\simon\CS-Learn\UCSD  Data Structure an Algorithms Specialisation\Data Structures\week2_priority_queues_and_disjoint_sets\2_job_queue\tests\02") as file:
    #     # Read the first line (number of workers and jobs)
    #     n_workers, n_jobs = map(int, file.readline().split())
        
    #     # Read the second line (job durations)
    #     jobs = list(map(int, file.readline().split()))
    #     assert len(jobs) == n_jobs

    # # Assign jobs using the fast method
    # assign_jobs = fast_assign(n_workers, jobs)

    # for job in assign_jobs:
    #     print(job.worker,job.started_at)