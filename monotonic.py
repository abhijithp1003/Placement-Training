arr = [1, 2, 4, 5]  

increasing = True
decreasing = True

for i in range(len(arr) - 1):
    if arr[i] < arr[i + 1]:
        decreasing = False
    if arr[i] > arr[i + 1]:
        increasing = False

if increasing:
    print("Monotonic Non-Decreasing (Increasing)")
elif decreasing:
    print("Monotonic Non-Increasing (Decreasing)")
else:
    print("Not Monotonic")