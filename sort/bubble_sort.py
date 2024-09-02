def BubbleSort(arr,size):
    swapped = False
    for i in range(size-1):
        for j in range(size-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if not swapped:
            break
        

arr = []
size = int(input("Enter size of array : "))
for i in range(size):
    ele = int(input("Enter " + str(i) + " element : "))
    arr.append(ele)
print("Initial array : ")
print(arr)
BubbleSort(arr,size)
print("Sorted array : ")
print(arr)
