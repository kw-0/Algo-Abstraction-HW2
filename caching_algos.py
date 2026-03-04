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

    return hits


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

    return hits



def OPTFF(cache_size, requests):
    cache = []
    hits = 0

    for request in requests:
        if request in cache:
            hits += 1
        else:
            if len(cache) < cache_size:
                cache.append(request)
            else:
                future_requests = requests[requests.index(request) + 1:]
                future_cache = [item for item in cache if item in future_requests]
                # remove furthest in future request
                if future_cache:
                    to_remove = max(future_cache, key=lambda x: future_requests.index(x))
                    cache.remove(to_remove)
                else:
                    cache.pop(0)
                cache.append(request)
    return hits
