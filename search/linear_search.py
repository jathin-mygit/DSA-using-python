def LinearSearch(arr,size,key):
    for i in range(size):
        if arr[i] == key:
            globals()['pos'] = i
            return True
    return False
        
arr = []
size = int(input("Enter size of array : "))
for i in range(size):
    ele = int(input("Enter " + str(i) + " size of array : "))
    arr.append(ele)
key = int(input("Enter element to be found : "))

if LinearSearch(arr,size,key):
    print("\nElement found at index " + str(pos))
else:
    print("\nElement not found")
