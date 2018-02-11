#problem 69
n=int(input("Enter n valu:"))
k=int(input("Enter k valu:"))
l=sorted([int(input("Enter array[{0}]".format(i+1))) for i in range(n)])
print(*l[:n-k])
