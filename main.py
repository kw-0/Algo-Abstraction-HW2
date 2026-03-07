from caching_algos import FIFO, LRU, OPTFF

if __name__ == "__main__":
    capacity, m = input("Cache Capacity and Number of Requests (m): ").split()
    if capacity == "" or m == "":
        print("No cache capacity or m provided")
        capacity = 0
        m = 0
    else:
        capacity = int(capacity)
        m = int(m)

    # requests = list(map(int, input("Requests: ").split()))
    requests = random_

    FIFO_misses = FIFO(capacity, requests)
    LRU_misses = LRU(capacity, requests)
    OPTFF_misses = OPTFF(capacity, requests)

    print(f"FIFO  : {FIFO_misses}")
    print(f"LRU   : {LRU_misses}")
    print(f"OPTFF : {OPTFF_misses}")

