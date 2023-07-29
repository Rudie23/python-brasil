
def collazt(n):
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n
        if n == 1:
            break


def collatz_len(n):
    count = 0
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
        if n == 1:
            break


def example_collatz():
    n = 7
    seq = list(collazt(n))
    print(seq)
    # If you jus want the length of the list
    print(sum(1 for _ in collazt(n)))


example_collatz()
