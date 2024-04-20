import array

arr = array.array('i',map(int,input().split(" ")))
print (arr)
# print("Using inbuilt to reverse an array: ")
# arr.reverse()
# for i in arr:
#     print(i,end=' ')

# print( )
# print("By printing array in reverse order: ")
# for i in range(len(arr),0,-1):
#     print(arr[i-1], end=' ')

print("Logical product: ")
i = 0
j= len(arr)-1

while(i!=j or i<j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    i+=1
    j-=1

for k in arr:
    print(k)