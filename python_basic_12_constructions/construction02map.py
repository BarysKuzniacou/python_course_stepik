x,y,z = input().strip().split()

print(f'{x=} {y=} {z=}')

x, y, z = map(int, (x, y, z))

print(f'volume = {x * y * z}')

x2,y2,z2 = map(int, input().strip().split())

print(f'volume = {x2 * y2 * z2}')