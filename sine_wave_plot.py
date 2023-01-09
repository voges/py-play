"""Code demonstrating matplotlib's pyplot interface."""


import math
import matplotlib.pyplot as plt


def main():
    """Plot a sine wave."""
    plt.ioff()
    sample_locs = [x / 1000 for x in range(1000)]
    sine_vals = [math.sin(2 * math.pi * s) for s in sample_locs]
    plt.plot(sample_locs, sine_vals, linestyle="--")
    plt.show()


if __name__ == "__main__":
    main()
