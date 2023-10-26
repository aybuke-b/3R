import time
from rich import print as rprint


def timer(func):
    """`timer`: This function  allows to be passed as a @decorator and gives the elapsed time of a function afterwards.

    ---------
    `Parameters`
    --------- ::

        func (function): # Any function basically

    `Example(s)`
    ---------

    >>> @timer
    >>> def func(a:int)-> list[int]:
    >>>     return [a for a in range(1000000)]
    >>> func(2)
    ... #Elapsed time for func function: 0.041 seconds."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        rprint(
            f"[italic]Elapsed time[/italic] for [bold red]{func.__name__}[/bold red] function: {round(elapsed_time,3)} seconds."
        )
        return result

    return wrapper
