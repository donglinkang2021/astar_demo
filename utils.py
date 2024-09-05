import time

def calc_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} cost time {end_time - start_time: .5f}s", end=" ")
        return result
    return wrapper