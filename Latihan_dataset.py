from sklearn import datasets
from sklearn.model_selection import train_test_split

iris=datasets.load_iris()
x=iris.data
y=iris.target
print(len(x))
print(len(y))
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2)
"""
iris=>150 data 
testing=>0.2*150->30
train=>120
"""
print("\nX")
print(len(X_train))
print(len(X_test))

print("\nY")
print(len(Y_train))
print(len(Y_test))
print("\n")

for i in range(3):
    X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2)
    print(X_test)

for i in range(3):
    X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2)
    print(Y_test)

