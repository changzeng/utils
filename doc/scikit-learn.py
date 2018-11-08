# 决策树
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# 逻辑回归
from sklearn import linear_model
model = linear_model.LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')
model.fit(X, Y)

# K折
from sklearn.cross_validation import KFold
for _train, _test in KFold(25, n_folds=5, shuffle=True):
	_train_samples = data[_train]
	_test_samples = data[_test]

# 打印精度
from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred)

# 交叉验证
from sklearn.cross_validation import cross_val_score
model = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(model, X, y, cv=10, scoring='accuracy')

# 独热编码
from sklearn import preprocessing
enc = preprocessing.OneHotEncoder()
enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
enc.transform([[0, 1, 3]]).toarray()
# 结果：array([[ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  1.]])
