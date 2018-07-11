class node:
    
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setData(self, data):
        self.data = data

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, val):
        n = node(val)
        curr = self.root
        if(self.root == None):
            self.root = n
        else:
            while(curr):
                if(curr.data < n.data):
                    prev = curr
                    curr = curr.right
                else:
                    prev = curr
                    curr = curr.left
                    
            if(prev.data > n.data):
                prev.left = n
            else:
                prev.right = n

    def findMax(self, rt):
        if(rt.right != None):
            self.findMax(rt.right)
        else:
            print(rt.getData())

            
    def findMin(self, rt):
        if(rt.left != None):
            self.findMin(rt.left)
        else:
            print(rt.getData())

    def inorder(self, rt):
        #print("Entered: ", rt.data)
        if(rt.left != None):
            self.inorder(rt.left)
        print(rt.data)
        if(rt.right != None):
            self.inorder(rt.right)

    def preorder(self, rt):
        #print("Entered: ", rt.data)
        print(rt.data)
        if(rt.left != None):
            self.preorder(rt.left)
        if(rt.right != None):
            self.preorder(rt.right)

    def postorder(self, rt):
        #print("Entered: ", rt.data)
        if(rt.left != None):
            self.postorder(rt.left)
        if(rt.right != None):
            self.postorder(rt.right)
        print(rt.data)
            
        
t = Tree()
t.insert(5)
t.insert(3)
t.insert(2)
t.insert(4)
t.insert(7)
t.insert(6)
t.insert(8)

t.findMax(t.root)
t.findMin(t.root)
print()
t.inorder(t.root)
print()
t.preorder(t.root)
print()
t.postorder(t.root)
