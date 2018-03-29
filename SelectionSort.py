def selectionSort(a):
    length = len(a)
    for i in range(0,length-1):
        for j in range(i+1,length):
            if(a[i]>a[j]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp

arr = [3,1,5,7,2,1,5]
selectionSort(arr)
print(arr)
