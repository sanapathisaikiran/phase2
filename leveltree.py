
def printlevelorder(root):
    if root==None:
        return
    Q=[root]
    result=[]
    while len(Q):
        n=len(Q)
        subresult=[]
        for i in range(n):
            #deletion
            currnode=Q.pop(0)
            #append
            subresult.append(currnode.data)
            #for left
            if currnode!=None:
                Q.append(currnode.left)
            #forright
            if currnode!=None:
                Q.append(currnode.right)
        result.append(subresult)
    print(result)
