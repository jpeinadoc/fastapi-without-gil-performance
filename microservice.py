import asyncio
from fastapi import FastAPI
import math
from concurrent.futures import ThreadPoolExecutor
from time import time
from multiprocessing import Pool

app = FastAPI()

def compute_pi(iterations: int) -> float:
    result = 0.0
    for k in range(iterations):
        result += 4.0 * (-1)**k / (2*k + 1)
    return result

@app.get("/compute-pi/")
def compute(iterations: int = 100_000_000):
    start_time = time()
    result = compute_pi(iterations)
    duration = time() - start_time
    return {"pi_approximation": result, "time_taken": duration}

@app.get("/compute-pi-parallel/")
def compute_parallel(iterations: int = 100_000_000, threads: int = 4):
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



@app.get("/compute-pi-parallel-mp/")
def compute_parallel_mp(iterations: int = 100_000_000, processes: int = 4):
    start_time = time()
    step = iterations // processes
    with Pool(processes=processes) as pool:
        results = pool.map(compute_pi, [step] * processes)
    result = sum(results)
    duration = time() - start_time
    return {"pi_approximation": result, "time_taken": duration, "processes": processes}

@app.get("/execute-event-loop")
async def execute_task(iterations: int = 100_000_000, threads: int = 4):
    start_time = time()
    step = iterations // threads
    
    # Crear el ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=threads) as executor:
        # Ejecutar cálculos en paralelo

        # Obtener el Event Loop actual
        loop = asyncio.get_running_loop()
        futures = [
            loop.run_in_executor(executor, compute_pi, step)
            for _ in range(threads)
        ]
        results = await asyncio.gather(*futures)  # Esperar todos los resultados

    result = sum(results)
    duration = time() - start_time
    return {"pi_approximation": result, "time_taken": duration, "threads": threads}

