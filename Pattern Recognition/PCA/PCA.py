import numpy as np

from Read_mat_file.ReadMatFile import *


class PCA:

    def __init__(self, sample, lower_dimension):
        xs = sample

        # step1：对样本去均值，进行中心化
        X = xs[0]  # 将样本中所有向量横向拼接
        for i in range(1, len(xs)):
            X = np.hstack((X, xs[i]))
        avg = np.mean(X, axis=1)
        X_adj = X - avg

        # step2：求特征协方差矩阵
        sigma = np.cov(X_adj)  # sigma是协方差矩阵

        # step3：求协方差矩阵的 特征值 和 特征向量
        eigen_value, feature_vectors = np.linalg.eig(sigma)

        # step4：将 特征值-特征向量 对按特征值从大到小排序，选择前lower_dimension个
        eigen_feature_list = []
        for i in range(len(eigen_value)):
            eigen_feature_list.append((eigen_value[i], feature_vectors[i]))
        eigen_feature_list = sorted(eigen_feature_list, key=lambda tuple: tuple[0], reverse=True)

        # step5：合并前lower_dimension个特征向量得到降维变换矩阵(dimension_reduction_mat)lower_dimension*orig_dimension
        dimension_reduction_mat = eigen_feature_list[0][1]
        for i in range(1, lower_dimension):
            dimension_reduction_mat = np.vstack((dimension_reduction_mat, eigen_feature_list[i][1]))

        # step6：进行降维变换
        lower_xs = []
        for x in xs:
            lower_x = np.matmul(dimension_reduction_mat, x)
            lower_xs.append(lower_x)
        self.lower_sample = lower_xs
