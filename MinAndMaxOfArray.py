brr = list(map(int, input().split(' ')))
brr.sort()

min = brr[0]
max = brr[len(brr)-1]

print("Minimum of Array is: ",end =' ')
print(min)

print("Maximum of array is: ",end=' ')
print(max)