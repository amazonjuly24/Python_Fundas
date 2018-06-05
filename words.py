fname=input("Enter the file name:")
num=0
with open(fname,'r') as f:
    for line in f:
        words=line.split()
        num+=len(words)
print(num)
