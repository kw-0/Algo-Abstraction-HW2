import random
from caching_algos import FIFO, LRU, OPTFF

def generate_size_and_requests():
    cache_size = random.randint(5, 20)

    requests = []
    for _ in range(100):
        requests.append(random.randint(1, 20))
    return cache_size, requests

def run_gen():
    num_tests = 3
    for i in range(num_tests):
        cache_size, requests = generate_size_and_requests()

        with open(f"file{i+1}.in", "w") as f:
            f.write(f"{cache_size} {len(requests)}\n")
            f.write(" ".join(map(str, requests)))

run_gen()