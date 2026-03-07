def FIFO(cache_size, requests):
    cache = []
    hits = 0

    for request in requests:
        if request in cache:
            hits += 1
        else:
            if len(cache) < cache_size:
                cache.append(request)
            else:
                cache.pop(0)
                cache.append(request)

    return len(requests)-hits

def LRU(cache_size, requests):
    cache = []
    hits = 0

    for request in requests:
        if request in cache:
            hits += 1
            cache.remove(request)
            cache.append(request)
        else:
            if len(cache) < cache_size:
                cache.append(request)
            else:
                cache.pop(0)
                cache.append(request)

    return len(requests)-hits

def OPTFF(cache_size, requests):
    cache = []
    hits = 0

    for i, request in enumerate(requests):
        if request in cache:
            hits += 1
        else:
            if len(cache) < cache_size:
                cache.append(request)
            else:
                future_requests = requests[i+1:]
                distances = []
                # reverse_future_requests = future_requests[::-1]
                # future_cache = []
                for item in cache:
                    if item in future_requests:
                        distances.append(future_requests.index(item))
                    else:
                        distances.append(float('inf'))

                # remove farthest in future
                to_remove = cache[distances.index(max(distances))]
                cache.remove(to_remove)
                cache.append(request)

    return len(requests)-hits