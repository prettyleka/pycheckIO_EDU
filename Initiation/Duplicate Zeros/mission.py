from typing import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    zeroes=donuts.count(0)
    i=0
    l=len(donuts)
    while i<l+zeroes:
        if donuts[i] == 0:
            donuts.insert(i+1, 0)
            i+=2
        else:
            i+=1

    return donuts


print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))

assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")
