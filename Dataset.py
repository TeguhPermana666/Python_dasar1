from sklearn.model_selection import train_test_split

X_Data=range(10)#0,1,2,3,4,5,6,7,8,9
Y_Data=range(10)

print("Random state ditentukan")
X_train,X_test,Y_train,Y_test=train_test_split(X_Data,Y_Data,test_size=0.3,random_state=42)
#train|testing ,train | testing
print(X_train)
print(X_test)
print(Y_train)
print(Y_test)

print("Y-Train")
for i in range(3):
    X_train,X_test,Y_train,Y_test=train_test_split(X_Data,Y_Data,test_size=0.3,random_state=42)
    print(Y_train)

print("X-Train")
for i in range(3):
    X_train,X_test,Y_train,Y_test=train_test_split(X_Data,Y_Data,test_size=0.3,random_state=42)
    print(X_train)


print("\nY-test\n")
for i in range(3):
    X_train,X_test,Y_train,Y_test=train_test_split(X_Data,Y_Data,test_size=0.3,random_state=42)
    print(Y_test)
print("\nX-test\n")
for i in range(3):
    X_train,X_test,Y_train,Y_test=train_test_split(X_Data,Y_Data,test_size=0.3,random_state=42)
    print(X_test)



print("\n\n Random state tidak ditentukan")
X_train,X_test,Y_train,Y_test=train_test_split(X_Data,Y_Data,test_size=0.3,random_state=None)
print(X_train)
print(X_test)
print(Y_train)
print(Y_test)

print("Y-Train")
for i in range(3):
    X_train,X_test,Y_train,Y_test=train_test_split(X_Data,Y_Data,test_size=0.3,random_state=None)
    print(Y_train)
print("X-Train")
for i in range(3):
    X_train,X_test,Y_train,Y_test=train_test_split(X_Data,Y_Data,test_size=0.3,random_state=None)
    print(X_train)



print("\nY-test\n")
for i in range(3):
    X_train,X_test,Y_train,Y_test=train_test_split(X_Data,Y_Data,test_size=0.3,random_state=None)
    print(Y_test)

print("\nX-test\n")

for i in range(3):
    X_train,X_test,Y_train,Y_test=train_test_split(X_Data,Y_Data,test_size=0.3,random_state=None)
    print(X_test)