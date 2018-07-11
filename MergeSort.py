def mergeSort(arr):
    mid = int(len(arr) / 2)
    if(mid > 0):
        a = mergeSort(arr[:mid])
        b = mergeSort(arr[mid:])
        c = merge(a, b)
    else:
        c = arr
    return c

def merge(a, b):
    c = []
    while(a and b):
        if(a[0] < b[0]):
            c.append(a[0])
            del(a[0])
        else:
            c.append(b[0])
            del(b[0])
    if(a == []):
        c.extend(b)
    else:
        c.extend(a)
    return c

a = [5,4,2,3,1,7,4,5,34,5,6,7,54,3,2,4,5,3,2,1,4,5,6,7,3,2,4,5,5,5,4,3,3,34,5,4,3,3,5,4,3,3,45,4,2,4,5,6,6,7,5,4,3,3,5,6,7,8,9,9,9,0,6,5]
result = mergeSort(a)
print(result)
        
    
