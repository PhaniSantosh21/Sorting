def radixSort(arr):
    #Converting list of numbers to list of strings by appending zeros in the beginning.
    maxValue = max(arr)
    length = len(str(maxValue))
    print(length)
    arr1 = []
    for i in arr:
        arr1.append(str(i).zfill(length))

    #Distributing into buckets depending on the values
    for i in range(0, length):
        dic = {'0':[], '1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[]}
        a = []
        for j in range(0, len(arr1)):
            dic[arr1[j][length-1-i]].append(arr1[j])

        #Gathering the values from buckets after each iteration.
        for k in dic:
            a.extend(dic[k])
        arr1 = a

    #Converting list of strings to list of numbers    
    arr = []
    for i in arr1:
        arr.append(int(i))
        

arr = [1,55,32,107,65,999,8,1000]
radixSort(arr)
print(arr)
