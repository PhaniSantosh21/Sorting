class queue:
    que = []
    queLen = 5
    def insertQue(self, a):
        if(len(self.que) == self.queLen):
            print("Queue is full")
        else:
            self.que.append(a)

    def deleteQue(self):
        if(len(self.que) == 0):
            print("Queue is empty")
        else:
            self.que.remove(self.que[0])

    def printQue(self):
        print(self.que)


a = queue()
a.insertQue(1)
a.insertQue(2)
a.insertQue(3)
a.insertQue(4)
a.insertQue(5)
a.insertQue(6)
a.deleteQue()
a.printQue()
a.deleteQue()
a.deleteQue()
a.deleteQue()
a.deleteQue()
a.deleteQue()

