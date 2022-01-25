from sklearn import datasets
#buat data set
iris=datasets.load_iris()

x=iris.data #data set
y=iris.target #data label

#membuat modul
from sklearn import tree

clf=tree.DecisionTreeClassifier()

#make validation cross
from sklearn.model_selection import cross_val_score
scores=cross_val_score(clf,x,y,cv=5)
#cetak analisis dari validation state dengan validation cross
print(scores)
nilai=0
for i in range(len(scores)):
    nilai=nilai+scores[i]
nilai=nilai/len(scores)
print(nilai)
#rata rata hasil dari evaluasi modul adalah dengan validasi kelipatan-k (5) adalah 0.9600000000000002
#0.9600000000000002 mendekati 1 yang berarti object sangat berpengaruh terhdp sampel yg berarti
#modul desicison tree sangat optimal jika digunakan pada dataset iris.


