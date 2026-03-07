from caching_algos import FIFO, LRU, OPTFF

def read_input_file(filepath):
    with open(filepath, "r") as f:
        cache_size, num_requests = map(int, f.readline().split())
        requests = list(map(int, f.readline().split()))

    return cache_size, requests

cache_size, requests = read_input_file("file1.in")


def run():
    input_files = ["file1.in", "file2.in", "file3.in"]
    with open("out.txt", "w") as out:
        for i, filename in enumerate(input_files):
            cache_size, requests = read_input_file(filename)

            FIFO_misses = FIFO(cache_size, requests)
            LRU_misses = LRU(cache_size, requests)
            OPTFF_misses = OPTFF(cache_size, requests)

            output = f"""File{i+1}
            k = {cache_size}
            m = {len(requests)}
            FIFO - {FIFO_misses}
            LRU - {LRU_misses}
            OPTFF - {OPTFF_misses}
            """
            print(output)
            out.write(output)

run()
