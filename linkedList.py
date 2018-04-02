class node:
    value = None
    link = None
    
    def setValue(self,key):
        self.value = key
        
    def setLink(self,a):
        self.link = a


class linkedList:
    head = None
    tail = None
    length = 0
    def __init__(self):
        head = None
        tail = None
        length = 0

    def addNode(self,a):
        new = node()
        new.setValue(a)
        self.length += 1
        if(self.head == None):
            self.head = new
            self.tail = new
        else:
            self.tail.link = new
            self.tail = new

    def printList(self):
        i = self.head
        if(self.head == None):
            print("List is empty")
        while(i != None):
            print(i.value)
            i = i.link
        print("\n")


    def insertNode(self, val, pos):
        if(pos <= 0 or pos >= self.length):
            print("Invalid position")
        elif(self.length >= pos):
            new = node()
            new.setValue(val)

            n = node()
            n = self.head
            if(pos==1):
                self.head = new
                new.link = n
            else:
                i = 0
                while(i < pos-2):
                    i += 1
                    n = n.link
                new.link = n.link
                n.link = new
                self.length += 1

    def deleteNode(self, val):
        cur = node()
        prev = node()
        cur = self.head
        prev = self.head
        if(cur.value == val):
            self.head = cur.link
            return
        while(cur != None):
            if(cur.value == val):
                prev.link = cur.link
                break
            elif(self.head == cur):
                cur = cur.link                
            else:
                prev = prev.link
                cur = cur.link
        if(cur == None):
            print("Element not found")
                

l = linkedList()
l.addNode(5)
l.addNode(4)
l.addNode(3)
l.printList()
l.insertNode(6,1)
l.printList()
l.deleteNode(4)
l.printList()
l.deleteNode(3)
l.printList()
l.deleteNode(6)
l.printList()
l.deleteNode(6)
l.printList()
l.deleteNode(5)
l.printList()


