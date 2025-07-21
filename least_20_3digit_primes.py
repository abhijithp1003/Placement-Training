import math

count = 0
for i in range(100, 1000):
    is_prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")
        count += 1
        if count == 20:
            break 