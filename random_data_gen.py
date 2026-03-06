# generate random cache and requests
# run each algo on the random inputs
# measure the misses
# first three random example input and output put into example.in and example.out

import random

from caching_algos import FIFO, LRU, OPTFF

def generate_size_and_requests():
    cache_size = random.randint(1, 10)
    requests = []
    for _ in range(random.randint(1, 20)):
        requests.append(random.randint(1, 20))
    return cache_size, requests

def run_gen():
    num_tests = 3

    for i in range(num_tests):
        cache_size, requests = generate_size_and_requests()
        FIFO_hit = FIFO(cache_size, requests)
        LRU_hit = LRU(cache_size, requests)
        OPTFF_hit = OPTFF(cache_size, requests)
        output = f"Cache Size = {cache_size}\n Requests = {requests}\n Misses:\n Fifo - {len(requests) - FIFO_hit}\n LRU - {len(requests) - LRU_hit}\n OPTFF - {len(requests) - OPTFF_hit} "
        print(output)


run_gen()
