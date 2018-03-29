def linearSearch(arr, key):
    flag = 0
    for i in arr:
        if(i == key):
            print("Element Found")
            flag = 1
    if(flag == 0):
        print("Element Not Found")

arr = [2,4,6,8,0,1,3,5,7,9]
key = [0,11,7,-19,3,99]
for i in key:
    linearSearch(arr, i)
