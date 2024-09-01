pos = -1
def BinarySearch(arr,key):
    low = 0
    high = len(arr)-1
    for i in (low,high):
        mid = (low+high) // 2
        if arr[mid] == key:
            globals()['pos'] = mid
            return True
        else:
            if arr[mid] < key:
                low = mid+1
            else:
                high = mid-1

arr = []
size = int(input("Enter size of array : "))
for i in range(size):
    ele = int(input("Enter element " + str(i) + " :"))
    arr.append(ele)
key = int(input("Enter element to be found : "))
if BinarySearch(arr,key):
    print("Element found at index " + str(pos))
else:
    print("Element not found")

