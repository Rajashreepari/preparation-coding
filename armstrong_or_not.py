def is_armstrong(n):
    l=len(str(n))
    temp=n
    res=0
    while(n>0):
        remainder=n%10
        res+=remainder**l
        n//=10
    if res==temp:
        print(f"{temp} is Armstrong Number")
    else:
        print(f"{temp} is not Armstrong Number")

n=int(input("Enter number:"))
is_armstrong(n)