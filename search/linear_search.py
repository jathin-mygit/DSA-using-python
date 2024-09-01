def LinearSearch(arr,size,key):
    for i in range(size):
        if arr[i] == key:
            print("\nElement found!")
            return
    print("\nElement not found!")
        
arr = []
size = int(input("Enter size of array : "))
for i in range(size):
    ele = int(input("Enter " + str(i) + " size of array : "))
    arr.append(ele)
key = int(input("Enter element to be found : "))
for i in range(size):
    print(arr[i], end=" ")
LinearSearch(arr,size,key)
