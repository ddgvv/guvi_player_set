#problem 65
n=int(input("Enter n valu:"))
l=sorted([int(input("Enter array[{0}]".format(i+1))) for i in range(n)])
print(*[i for i in l if i<n])
