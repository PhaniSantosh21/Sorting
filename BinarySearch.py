def binarySearch(arr, key, start, end):
    if(start <= end):
        mid = int((start+end)/2);
        if(arr[mid]== key):
            print("Element Found")
        elif(arr[mid] > key):
            binarySearch(arr, key, start, mid-1)
        else:
            binarySearch(arr, key, mid+1, end)
    else:
        print("Element Not Found")

arr = [0,1,2,3,4,5,6,7,8,9]
key = [0,11,7,-19,3,99]
for i in key:
    binarySearch(arr, i, 0, len(arr)-1)

