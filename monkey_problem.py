from math import ceil
def cal(x, a, b):
    return ceil((x - a) / (a - b)) * 2 + 1



print(cal(30, 10, 5))
print(cal(25, 7, 4))
print(cal(25, 9, 3))