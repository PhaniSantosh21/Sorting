def insertSort(a):
    length = len(a)
    for i in range(1,length):
        temp = a[i]
        for j in range(0,i+1):
            if(a[i-j-1]>temp):
                a[i-j] = a[i-j-1]
            else:
                break
        a[i-j] = temp
    
arr = [10,6,4,2,9,7,5]
insertSort(arr)
print(arr)
