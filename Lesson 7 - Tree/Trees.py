class TreeNode:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    # Insertion operation
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    # Search Operation
    def search(self,value):
        if(value < self.data):
            if self.data is None:
                return str(value) + "Not found, tree is empty"
            return self.left.search(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + " not found"
            return self.right.search(value)
        else:
            print(str(self.data) + 'is found')

    #Inorder
    def inorder(self):
        # Follow from left subtree to root to right subtree
        if self.left:
            self.left.inorder()
        
        print(self.data, " -> ",end=" ")

        if self.right:
            self.right.inorder()

    #Preorder
    def preorder(self):
        # Follow from root to left subtree to right sub tree
        print(self.data)
        
        if(self.left):
            self.left.inorder()
        if(self.right):
            self.right.inorder()

    #Postorder
    def postorder(self):
        # Follow from right sub tree to left sub tree to finally root

        if(self.right):
            self.right.inorder()
        if(self.left):
            self.left.inorder()

        print (self.data)

treeNode1 = TreeNode(10)
treeNode1.insert(2)
treeNode1.insert(12)
treeNode1.insert(3)
treeNode1.insert(13)

treeNode1.search(2)