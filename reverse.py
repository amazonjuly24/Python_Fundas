#Reverse a given number

n=int(input("Enter the number to reverse:"))

b=0

while(n>0):
    a=int(n%10)
    b=int(b*10)+a
    n=n/10
print(b)

