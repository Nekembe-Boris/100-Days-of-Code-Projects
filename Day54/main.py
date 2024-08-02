from time import time as dt
current_time = dt()
print(current_time) # seconds since Jan 1st, 1970

def speed_calc_decorator(func):
    start_time = dt()
    func()
    end_time = dt() - start_time
    print(f"{func.__name__} run speed: {end_time}s")

@speed_calc_decorator
def fast_function():
    for _ in range(1000000):
        pass

@speed_calc_decorator
def slow_function():
    for _ in range(10000000):
        pass
