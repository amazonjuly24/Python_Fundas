

mark=[]
for i in range(1,6):
    m1=int(input("Enter the marks obtained in subject {}:".format(i)))
    mark.append(m1)


m=sum(mark)
avg=m/5
print(avg)
if(avg>=90):
    print("Grade-->S")
elif(avg>= 80 & avg<90):
    print("Grade A")
elif(avg>= 70 & avg<80):
    print("Grade B")
elif(avg>= 60 & avg<70):
    print("Grade C")
elif(avg> 60 & avg<50):
    print("Grade D")
else:
    print("fail")

