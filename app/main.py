import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}


    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tuple_kwargs = tuple(kwargs.items())
        total_data = (args, tuple_kwargs)
        if total_data not in memory:
            memory[total_data] = func(*args, **kwargs) # (1,2,3): (1,2,3)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return memory[total_data]
    return wrapper





def getting_from_cache(*args,**kwargs):
    return f"{args},{kwargs}"
