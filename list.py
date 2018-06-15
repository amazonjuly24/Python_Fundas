import itertools
#list of fruits
fruit=['apple','mango','grapes','banana', 'strawberry', 'cherry'] 
print("Fruit list-->",fruit)
#join method
print((" ".join(fruit)))

#partitioning the list
fruit=['apple','mango','grapes','banana', 'strawberry', 'cherry', 'jack','watermelon']
part = list(zip(*[iter(fruit)]*3))
print(part)

#more then one list
sname=['john','jane', 'jim', 'tom', 'jerry','duck' , 'dev','pappu', 'Mark','harry']
sno=[101,102,103,104,105,106,107,108,109,110,111]
code=[111,222,333,444,555,666]
for a, b, c in zip(sname, sno, code):
    print(a, b,c)

#take string and convert into list
#convert string
convert=list(map(str,raw_input().split()))
print(convert)


#convert list of list into single list
num = [[1, 2], [3, 4], [5, 6],[7,8],[9,10]]
lst=list(itertools.chain.from_iterable(num))
print(lst)


 

