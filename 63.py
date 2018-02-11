#problem 63
n=int(input("Enter number:"))
list1=[int(input("Enter {0} element in List1:".format(i+1))) for i in range(n)]
list2=[int(input("Enter {0} element in List2:".format(i+1))) for i in range(n)]
print(*list(set(list1)&set(list2)))
