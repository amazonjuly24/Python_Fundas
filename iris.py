from sklearn import datasets
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt

#to load dataset
iris=datasets.load_iris()
print(iris)
print(iris['data'])
print(iris['target'])

#Visuvalizing sepal data
def visuvalize_sepal():
    x=iris.data[:,:2]
    y=iris.target
    #print(x)
    plt.scatter(x[:,0],x[:,1],c=y,cmap=plt.cm.coolwarm)
    plt.xlabel("sepal length")
    plt.ylabel("sepal width")
    plt.show()

visuvalize_sepal()
#Visuvalizing petal data
def visuvalize_petal():
    x=iris.data[:,2:]
    y=iris.target
    #print(x)
    plt.scatter(x[:,0],x[:,1],c=y,cmap=plt.cm.coolwarm)
    plt.xlabel("petal length")
    plt.ylabel("petal width")
    plt.show()

visuvalize_petal()



