from typing import Iterator


class Range:
    def __init__(self, stop: int):
        self.start = 0
        self.stop = stop

    def __iter__(self) -> Iterator[int]:
        curr = self.start
        while curr < self.stop:
            yield curr
            curr += 1


def range_example():
    for n in Range(10):
        print(n)


range_example()
