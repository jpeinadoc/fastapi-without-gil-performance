from concurrent.futures import ThreadPoolExecutor
from time import time

def compute_pi(iterations: int) -> float:
    result = 0.0
    for k in range(iterations):
        result += 4.0 * (-1)**k / (2*k + 1)
    return result


def compute_parallel(iterations: int = 100000000, threads: int = 20):
    start_time = time()
    step = iterations // threads
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [
            executor.submit(compute_pi, step)
            for _ in range(threads)
        ]
        result = sum(f.result() for f in futures)
    duration = time() - start_time
    return {"pi_approximation": result, "time_taken": duration, "threads": threads}

if __name__ == "__main__":
    print(compute_parallel())