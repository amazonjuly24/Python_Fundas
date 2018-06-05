#Number fo lines in file
fname=input("Enter the file name:")
num=0

with open(fname,'r') as f:
    for line in f:
        num+=1
print(num)
