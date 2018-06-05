fname=input("Enter the file name:")
f=open(fname,'a')

c=str(input("Enter the string to append"))
f.write("\n")
f.write(c)
f.close()

print("contents appended:")
f1=open(fname,'r')
l=f1.readline()
while(l!=""):
    print(l)
    l=f1.readline()
f1.close()
