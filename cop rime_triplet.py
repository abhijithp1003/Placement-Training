list_numbers=[1,2,2,3,4,4,4,5,6]
u=set(list_numbers)
for num in u:
    if num%2==0:
        list_numbers.remove(num)
print(list_numbers)