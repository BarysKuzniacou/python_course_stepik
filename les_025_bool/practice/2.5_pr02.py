import math
price = float(input())
price_int = math.trunc(price)
fractional_value = price - price_int
print(fractional_value > 0.5)