from concurrent.futures import ThreadPoolExecutor
from time import time
from multiprocessing import Pool

def compute_pi(iterations: int) -> float:
    result = 0.0
    for k in range(iterations):
        result += 4.0 * (-1)**k / (2*k + 1)
    return result


def compute_parallel_mp(iterations: int = 100000000, processes: int = 20):
    start_time = time()
    step = iterations // processes
    with Pool(processes=processes) as pool:
        results = pool.map(compute_pi, [step] * processes)
    result = sum(results)
    duration = time() - start_time
    return {"pi_approximation": result, "time_taken": duration, "processes": processes}


if __name__ == "__main__":
    print(compute_parallel_mp())