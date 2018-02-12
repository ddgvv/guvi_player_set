start,end=map(int,input("Enter the Start and End range:").split(' '))
print(sum([1 for i in range(start,end+1) if (i**0.5)%1==0 ]))
