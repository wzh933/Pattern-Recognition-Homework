from Read_mat_file.ReadMatFile import *


class PCA:

    def __init__(self, sample, lower_dimension):
        xs = sample
        X = xs[0]  # 将样本中所有向量横向拼接
        for i in range(1, len(xs)):
            X = np.hstack((X, xs[i]))
        sigma = np.cov(X)  # sigma是协方差矩阵
        sigma_1 = np.linalg.inv(sigma)  # 对协方差矩阵求逆
