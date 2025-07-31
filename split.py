def split_and_add(arr, k):
    return arr[k:] + arr[:k]

arr = [1, 2, 3, 4, 5, 6]
k = 2

result = split_and_add(arr, k)

print(result)