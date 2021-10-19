from math import sqrt

value_1, value_2 = input().split()
value_1 = int(value_1)
value_2 = int(value_2)
arithmetic_mean = (value_2 + value_1) / 2
geometric_mean = (sqrt(value_2 * value_1))
print("arithmetic mean:", arithmetic_mean)
print("geometric mean:", geometric_mean)
