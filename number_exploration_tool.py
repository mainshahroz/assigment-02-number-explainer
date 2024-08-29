import math
name = str(input("enter your name = "))
n1 = int(input("enter your first favorite number ="))
n2 = int(input("enter your second favorite number ="))
n3 = int(input("enter your third favorite number ="))

print(f"hello, {name} explore your favorite number")
list01 = []
list01.append(n1)
list01.append(n2)
list01.append(n3)
for i in list01:
   
    if i%2 == 0:
        print(f"the number {i} is even")
    elif i%2 != 0:
        print(f"the number {i} is odd")
    
for d in list01:    
    tuple=(d,d**2)
    print(f"the number is {d} and its square :{tuple}")
    


print(f"the sum of your favorite number is {n1+n2+n3}")
n = n1+n2+n3
if (n >=1 and n%2!=0) or (n==1) or (n == 2):
    print(f"{n} is a prime number") 

else:
    print(f"{n} is not prime number ")    