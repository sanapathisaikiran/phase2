class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def preorder(root):
    if root==None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)
obj1=node(100)
obj2=node(21)
obj3=node(-151)
obj4=node(87)
obj5=node(12)
obj6=node(52)
obj7=node(8)
obj8=node(27)
obj9=node(28)
obj10=node(7)

obj1.right=obj3
obj1.left=obj2
obj2.right=obj5
obj2.left=obj4
obj3.right=obj7
obj3.left=obj6
obj4.right=obj8
obj5.right=obj9
obj7.left=obj10
preorder(obj1)