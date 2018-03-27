def bubbleSort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)
    #return arr

#print("Enter the numbers you want to sort:")
#arr[] = input()
arr = [5,2,1,6,0,3,4]
print(arr)
bubbleSort(arr)
print(arr)
