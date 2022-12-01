"""This module tests different ways of measuring execution time."""


def test():
    """Stupid test function."""
    list(range(100))


if __name__ == "__main__":
    NUM_REPS = 1000000

    import timeit

    print(timeit.timeit("test()", number=NUM_REPS, setup="from __main__ import test"))

    import time

    start = time.time()
    for i in range(0, NUM_REPS):
        test()
    end = time.time()
    duration = end - start
    print(f"{duration}")
