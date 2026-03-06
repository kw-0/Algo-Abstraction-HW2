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

if __name__ == "__main__":
    main()
