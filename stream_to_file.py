"""Code showing how to write to a file."""


def main():
    """Write a test string to the file 'output.txt'."""
    with open("output.txt", mode="w", encoding="utf-8") as outfile:
        print("test output", file=outfile)


if __name__ == "__main__":
    main()
