"""Code that demonstrates variadic functions."""


def mean(*elems):
    """Compute the arithmetic mean of the elements."""
    return sum(elems) / len(elems)


def print_contacts(**contacts):
    """Print the contacts dictionary."""
    for name, contact in contacts.items():
        print(f"{name}: {contact}")


if __name__ == '__main__':
    print(f"mean = {mean(0, 1, 2, 3, 4, 5)}")
    print_contacts(Max="+49 511 12345", Moritz="+49 511 123456")
