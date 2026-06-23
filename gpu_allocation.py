import random
import time

class GPU:
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
        self.allocated_cores = 0

    def is_available(self, cores_needed):
        return self.allocated_cores + cores_needed <= self.capacity

    def allocate(self, cores_needed):
        if self.is_available(cores_needed):
            self.allocated_cores += cores_needed
            return True
        return False

    def deallocate(self, cores_to_release):
        self.allocated_cores = max(0, self.allocated_cores - cores_to_release)

    def __str__(self):
        return f"GPU {self.id} (Capacity: {self.capacity}, Allocated: {self.allocated_cores})"

class Job:
    def __init__(self, id, cores_required):
        self.id = id
        self.cores_required = cores_required

    def __str__(self):
        return f"Job {self.id} ({self.cores_required} cores)"

def simulate_allocation(gpus, jobs):
    print("--- Starting GPU Allocation Simulation ---")
    print("Available GPUs:")
    for gpu in gpus:
        print(f"  {gpu}")
    print("\nJobs to be allocated:")
    for job in jobs:
        print(f"  {job}")
    print("\n--- Allocation Process ---")

    allocated_jobs = {}
    unallocated_jobs = []

    # Simple greedy allocation strategy (demonstrates a basic allocation approach)
    for job in jobs:
        allocated = False
        # Try to find a GPU that can accommodate the job
        for gpu in gpus:
            if gpu.allocate(job.cores_required):
                allocated_jobs[job.id] = gpu.id
                print(f"Successfully allocated {job} to {gpu}")
                allocated = True
                break # Move to the next job once allocated
        if not allocated:
            unallocated_jobs.append(job)
            print(f"Failed to allocate {job}. No suitable GPU found.")

    print("\n--- Simulation Results ---")
    print("Allocated Jobs:")
    if allocated_jobs:
        for job_id, gpu_id in allocated_jobs.items():
            print(f"  Job {job_id} -> GPU {gpu_id}")
    else:
        print("  No jobs were allocated.")

    print("\nUnallocated Jobs:")
    if unallocated_jobs:
        for job in unallocated_jobs:
            print(f"  {job}")
    else:
        print("  All jobs were allocated.")

    print("\nFinal GPU Status:")
    for gpu in gpus:
        print(f"  {gpu}")

if __name__ == "__main__":
    # Define a set of GPUs with varying capacities
    gpu_pool = [
        GPU(id=1, capacity=16),
        GPU(id=2, capacity=32),
        GPU(id=3, capacity=8),
        GPU(id=4, capacity=32)
    ]

    # Define a list of jobs with different core requirements
    job_list = [
        Job(id=101, cores_required=10),
        Job(id=102, cores_required=20),
        Job(id=103, cores_required=5),
        Job(id=104, cores_required=15),
        Job(id=105, cores_required=25),
        Job(id=106, cores_required=10)
    ]

    # Run the simulation to demonstrate allocation challenges
    simulate_allocation(gpu_pool, job_list)

    print("\nThis simulation highlights how even with available GPU capacity,\npoor allocation strategies or fragmented resources can lead to unallocated jobs.\nThis is the core of the GPU allocation governance problem.")
