a=input("Enter the number : ")
i=len(a)
n=int(a)
odd=0
even=0
while(i>=0):
    a=n%10
    if(i%2==1):
        odd+=a
    else:
        even+=a
    i-=1
    n=n//10
print(even)
print(odd)
if(even==odd):
    print("It is magic number :")
else:
    print("It is not magic number :")