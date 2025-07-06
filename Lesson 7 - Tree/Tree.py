class TreeNode:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value
    
    def insert(self, key_value):
        if key_value < self.value:
            if self.left is None:
                self.left = TreeNode(key_value)
            else:
                self.left.insert(key_value)
        else:
            if self.right is None:
                self.right = TreeNode(key_value)
            else:
                self.right.insert(key_value)

    def preorder_traversal(self):
        print(self.value)

        if self.left:
            self.left.inorder_traversal()

        if self.right:
            self.right.inorder_traversal()

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()

        print(self.value)

        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()

        if self.right:
            self.right.inorder_traversal()

        print(self.value)
    
treeObj = TreeNode(10)

treeObj.insert(9)
treeObj.insert(3)
treeObj.insert(4)
treeObj.insert(8)

treeObj.insert(11)
treeObj.insert(12)
treeObj.insert(13)
treeObj.insert(14)

print("Preorder traversal")
treeObj.preorder_traversal()

print("\nInorder traversal")
treeObj.inorder_traversal()

print("\nPostOrder traversal")
treeObj.postorder_traversal()