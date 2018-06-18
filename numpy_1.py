#working with numpy
import numpy as np
arr=np.array([[1,2,3],[4,5,6]],dtype='float')
print("Array type",type(arr))
print("no of dimension:", arr.ndim)
print("Shape of array:",arr.shape)
print("size of array:",arr.size)
print("Array type",arr.dtype)
#creating array from tuple
b=np.array((1,1,1))
print(b)
#creating 3*4 array with all zeros
c=np.zeros((3,4))
print(c)
#creating array with complex values
d=np.full((3,3),7,dtype="complex")
print("complex array:",d)
#creating array with random values
e=np.random.random((3,3))
print("Random array:",e)
#creating sequence of integers with step of 3
f=np.arange(0,50,3)
print(f)
#Cretaing sequence of 10 values 
g=np.linspace(0,5,10)
print(g)
# Reshaping 3X4 array to 2X2X3 array
arry = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])
 
newarr = arry.reshape(2, 2, 3)
print(newarr)
#flatten array
flatarr=arr.flatten()
print(flatarr)

#dealing with array indexing

arr1 = np.array([[-1, 2, 0, 4, 5, 8,5],
                [4, -0.5, 6, 0, -4, 7,2],
                [2.6, 0, 7, 8, 2, 6,4],
                [3, -7, 4, 2.0, 5,2, -9]])

temp=arr1[:3,::3]
print("Array after slicing:",temp)

#boolean array indexing 
cond=arr1>0
temp=arr1[cond]
print("Element greater than zero:",temp)
print("Transpose:",arr1.T)
#dealing with unary operators
#Find maximum element in array
print("MAximum element:",arr1.max())
print("Row wise maximum:",arr1.max(axis=1))
print("column wise max:",arr1.max(axis=0))
print("Sum of array elements:",arr1.sum())
print("Cumulative sum of each row:",arr1.cumsum(axis=1))
#dealing with binary operators
a = np.array([[1, 2],
            [3, 4]])
b = np.array([[4, 3],
            [2, 1]])
print("Array sum:",a+b)
print("array mul:",a*b)
print("Matrix multiplication:",a.dot(b))

#universal functions(ufuncs like np.add, np.subtract, np.multiply, np.divide, np.sum, etc.)
print("Sine function:",np.sin(arr1))
print("cosine:",np.cos(arr1))
print("Exponential:",np.exp(arr))
print("Squart eoot:",np.sqrt(arr))

#Sorting array
x = np.array([[1, 4, 2],
                 [3, 4, 6],
              [0, -1, 5]])

print("Array in sorted order:",np.sort(x,axis=None))
#row wise sort(axis=1)
print("column wise sort:(Merge sort)",np.sort(x,axis=0,kind="mergesort"))
#Sorting in structured array
darray=[("name","S10"),("year",int),("cgpa",float)]
values=[('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7), 
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
arrr=np.array(values,dtype=darray)
print("Array sorted by name:\n",np.sort(arrr,order="name"))
print("Array sorted by year and cgpa:\n",np.sort(arrr,order=["cgpa","year"]))
