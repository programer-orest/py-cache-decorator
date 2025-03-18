import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args not in memory:
            memory[args] = func(*args, **kwargs) # (1,2,3): (1,2,3)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return memory[args]
    return wrapper





def getting_from_cache(*args):
    return args
