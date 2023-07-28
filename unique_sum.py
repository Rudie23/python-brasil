import random
import time


def unique_sum_list(nums):
    total, seen = 0, list()
    for n in nums:
        if n in seen:
            continue
        total += n
        seen.append(n)
    return total


def unique_sum_tuple(nums):
    total, seen = 0, tuple()
    for n in nums:
        if n in seen:
            continue
        total += n
        seen = (*seen, n)
    return total


def unique_sum_dict(nums):
    total, seen = 0, dict()
    for n in nums:
        if n in seen:
            continue
        total += n
        seen[n] = None
    return total


def unique_sum_set(nums):
    total, seen = 0, set()
    for n in nums:
        if n in seen:
            continue
        total += n
        seen.add(n)
    return total, seen


# Faster using sum and set in one line code

def unique_sum_set_fast(nums):
    set_values = sum(set(nums))
    return set_values


def main():
    n = 100_000
    nums = [random.randint(0, 2 << 32) for _ in range(n)]
    for unique_sum in [
        unique_sum_tuple,
        unique_sum_list,
        unique_sum_dict,
        unique_sum_set,
    ]:
        start = time.perf_counter()
        total = unique_sum(nums)
        elapsed = time.perf_counter() - start
        print(f'{unique_sum.__name__}: {elapsed * 1000:.2f}')


main()
