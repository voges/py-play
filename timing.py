def test():
    """Stupid test function"""
    L = [i for i in range(100)]


if __name__ == '__main__':
    num_reps = 1000000

    import timeit
    print(timeit.timeit('test()', number=num_reps,
          setup='from __main__ import test'))

    import time
    start = time.time()
    for i in range(0, num_reps):
        test()
    end = time.time()
    duration = end - start
    print("{}".format(duration))
