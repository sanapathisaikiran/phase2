list=[36,78,90,87,67]
target=87
flag=0
n=len(list)
for index in range(n):
    if list[index]==target:
        flag=index
        break
if flag==0:
    print("target is not found")
else:
    print("target is at",flag)