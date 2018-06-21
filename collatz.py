def coll(n):

    if(n%2==0):
        n=n//2
    elif(n%2==1):
        n=(3*n)+1
    print(n)
        #coll(n)
    if(n>1):
        coll(n)
    
num=int(input("Enter the numebr:"))
coll(num)
