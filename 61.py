#problem 61
n=int(input("Enter n valu:"))
k=int(input("Enter k valu:"))
l=[int(input("Enter array[{0}]".format(i+1))) for i in range(n)]
print('yes' if sum(l)==k else 'no')
