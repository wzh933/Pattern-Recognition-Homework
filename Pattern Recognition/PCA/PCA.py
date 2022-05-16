import numpy as np

from Read_mat_file.ReadMatFile import *


class PCA:

    def __init__(self, sample, lower_dimension):
        X = sample

        # step1：对样本去均值，进行中心化
        print("step1：对样本去均值，进行中心化")
        avg = np.mean(X, axis=0)
        X_adj = X - avg  # 去均值

        # step2：求特征协方差矩阵
        print("step2：求特征协方差矩阵")
        sigma = np.cov(X_adj.transpose())  # sigma是协方差矩阵

        # step3：求协方差矩阵的 特征值 和 特征向量
        print("step3：求协方差矩阵的 特征值 和 特征向量")
        eigen_value, feature_vectors = np.linalg.eig(sigma)

        # step4：将 特征值-特征向量 对按特征值从大到小排序，选择前lower_dimension个
        print("step4：将 特征值-特征向量 对按特征值从大到小排序，选择前lower_dimension个")
        eigen_feature_list = []
        for i in range(len(eigen_value)):
            eigen_feature_list.append((eigen_value[i], feature_vectors[i]))
        eigen_feature_list = sorted(eigen_feature_list, key=lambda tuple: tuple[0], reverse=True)

        # step5：合并前lower_dimension个特征向量得到降维变换矩阵[dimension_reduction_mat]lower_dimension*orig_dimension
        print("step5：合并前lower_dimension个特征向量得到降维变换矩阵(dimension_reduction_mat)lower_dimension*orig_dimension")
        dimension_reduction_mat = np.array([eigen_feature_list[i][1] for i in range(lower_dimension)])
        print(dimension_reduction_mat)

        # step6：进行降维变换
        print("step6：进行降维变换")
        lower_X = np.matmul(X, dimension_reduction_mat.transpose()).astype(np.float)  # 避免出现复数

        self.data = lower_X
