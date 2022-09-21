# question: inverse BST (smaller -> right, bigger -> left) 

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def preorder(self):
        print(self.value)
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()
       
    def inorder(self):
        if self.left: self.left.inorder()
        print(self.value)
        if self.right: self.right.inorder()
    

def invert(root):
    if(root == None):
        return

    root.left, root.right = root.right, root.left
    
    invert(root.left)
    invert(root.right)


root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

root.preorder()
# a b d e c f 
print ("\n")
invert(root)
root.preorder()
# a c f b e d