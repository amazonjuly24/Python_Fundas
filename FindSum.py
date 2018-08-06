#To find summ of two element present in list
a=[10,5,23,7,6,2,8,3]
value=39
check=[]
b=sorted([x for x in a if x<value])
l=0
h=len(b)-1
while(l<h):
    s=b[l]+b[h]
    if(s==value):
        check.append(True)
        break 
    elif(s>value):
        h=h-1
    else:
        l=l+1
#print(check)
print(any(check))
