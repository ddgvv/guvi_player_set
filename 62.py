#problem 62
n=int(input("Enter number:"))
print(*[i for i in range(1,n) if (n/i)%2==1])
