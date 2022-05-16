import numpy as np
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from PCA import PCA

# 公开数据集
faces = datasets.fetch_olivetti_faces()

X = faces.data  # 数据
y = faces.target  # 标签

# -----------得到pca降维后的结果------------#
# pca_X = PCA(sample=X, lower_dimension=200).data
# np.save(file='pca_X.npy', arr=pca_X)
# ---------------------------------------#

pca_X = np.load('pca_X.npy')  # 降维后的数据

scaler = StandardScaler()  # 均值方差标准化

# 五折交叉检验
# 必须要洗牌打乱，不然在这个数据集里，训练集和测试集的label基本不相交
kf = KFold(n_splits=5, shuffle=True)

# 多层感知机（神经网络）对象，100隐层
clf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(100,), random_state=1, max_iter=500)
for train_index, test_index in kf.split(y):  # 划分数据集
    train_X, test_X = pca_X[train_index], pca_X[test_index]
    train_y, test_y = y[train_index], y[test_index]
    scaler.fit(train_X)  # 计算得到标准化的均值方差只在训练集做，根据sklearn官方文档：Don't cheat
    train_X = scaler.transform(train_X)  # 对训练集标准化
    test_X = scaler.transform(test_X)  # 对测试集标准化
    clf.fit(train_X, train_y)  # 模型训练
    predict_y = clf.predict(test_X)  # 模型预测
    acc = accuracy_score(predict_y, test_y)  # 得到预测准确率
    print('accuracy: {:.2%}'.format(acc))
