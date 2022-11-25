def mean(*elems):
    return sum(elems) / len(elems)


def print_contacts(**contacts):
    for name in contacts.keys():
        print("{}: {}".format(name, contacts[name]))


def main():
    print("mean = {}".format(mean(0, 1, 2, 3, 4, 5)))
    print_contacts(Max="+49 511 12345", Moritz="+49 511 123456")


if __name__ == '__main__':
    main()
