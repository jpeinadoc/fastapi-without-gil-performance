from time import time

def compute_pi(iterations: int) -> float:
    result = 0.0
    for k in range(iterations):
        result += 4.0 * (-1)**k / (2*k + 1)
    return result

def compute(iterations: int = 100000000):
    start_time = time()
    result = compute_pi(iterations)
    duration = time() - start_time
    return {"pi_approximation": result, "time_taken": duration}


if __name__ == "__main__":
    print(compute())