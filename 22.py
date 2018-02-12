num,k=map(int,input('Enter Two Number:').split(' '))
if num<k:
    num,k=k,num
print([i for i in range(1,k+1) if num%i==0 and k%i==0 ][-1])
