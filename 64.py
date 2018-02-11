#problem 64
n=int(input("Enter n valu:"))
k=int(input("Enter k valu:"))
l=sorted([int(input("Enter array[{0}]".format(i+1))) for i in range(n)])
print(*list(filter(lambda x: x<k ,l)))
