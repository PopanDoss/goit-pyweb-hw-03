import logging
import concurrent.futures
from time import time
from multiprocessing import cpu_count 

def factorize(*numbers):
    results = [] 

    start_time = time()
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()):
        for num in numbers:
            received = [i for i in range(1, num +1) if num % i == 0]
            results.append(received)

    end_time = time()
    
    logging.info(f"Час виконання: {end_time - start_time}")
    return results

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(message)s')
   
    numbers = (128, 255, 99999, 10651061)
    n = factorize(*numbers)

    for el in n:
        logging.info(el)