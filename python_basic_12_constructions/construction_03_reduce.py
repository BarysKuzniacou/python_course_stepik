from functools import reduce

volume = reduce(
    lambda x, y: x * y,
    map(int, input().strip().split())
)

print(f'{volume = }')