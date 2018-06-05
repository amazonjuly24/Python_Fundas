a=str(input("Enter the text file:"))
file=open(a,'r')
line=file.readline()
while(line!=""):
    print(line)
    line=file.readline()
file.close()
