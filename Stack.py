class stack:
    arr = []
    stackLen = 5
    def push(self, a):
        if(len(self.arr) == self.stackLen):
            print("Stack is full")
        else:
            self.arr.append(a)
        
    def pop(self):
        if(self.arr == []):
            print("Stack is empty")
        else:
            self.arr.pop()
        
    def printStack(self):
        print(self.arr)

a = stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.push(6)
a.printStack()
a.pop()
a.printStack()
a.pop()
a.pop()
a.pop()
a.pop()
a.pop()
