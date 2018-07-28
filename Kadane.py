class Kadane:
    def __init__(self, arr):
        self.a = arr
        self.Max = 0
        #self.maxArr = []
        self.beg = 0
        self.end = 0
    def maxSum(self):
        end = len(self.a)
        for i in range(end):
            total = 0
            for j in range(i, end):
                total += self.a[j]
                if(total > self.Max):
                    self.Max = total

    def printMaxSum(self):
        print(self.Max)

    def KadaneAlgo(self):
        temp = 0
        self.Max = 0
        tempArr = []
        self.beg = 0
        for i in range(len(self.a)):
            temp += self.a[i]
            #tempArr.append(a[i])
            if(temp < 0):
                temp = 0
                #tempArr = []
                self.beg = i + 1
                #print(self.maxArr)
            if(self.Max < temp):
                self.Max = temp
                #self.maxArr = tempArr[:]
                self.end = i
            #print(self.maxArr)

    def printMaxArr(self):
        print(self.a[self.beg:self.end+1])

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
c = Kadane(a)
c.maxSum()
c.printMaxSum()
c.KadaneAlgo()
c.printMaxSum()
c.printMaxArr()
