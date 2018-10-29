# 决策树
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# K折
from sklearn.cross_validation import KFold
kf = KFold(25, n_folds=5, shuffle=True)
for _train, _test in kf:
	_train_samples = data[_train]
	_test_samples = data[_test]

# 打印精度
from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred)

# 交叉验证
from sklearn.cross_validation import cross_val_score
model = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(model, X, y, cv=10, scoring='accuracy')
