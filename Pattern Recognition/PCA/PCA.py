import numpy as np

from Read_mat_file.ReadMatFile import *


class PCA:

    def __init__(self, sample, lower_dimension):
        xs = sample

        # step1：对样本去均值，进行中心化
        print("step1：对样本去均值，进行中心化")
        X = xs[0]  # 将样本中所有向量竖向拼接
        for i in range(1, len(xs)):
            X = np.vstack((X, xs[i]))
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
        dimension_reduction_mat = eigen_feature_list[0][1]
        for i in range(1, lower_dimension):
            dimension_reduction_mat = np.vstack((dimension_reduction_mat, eigen_feature_list[i][1]))

        # step6：进行降维变换
        print("step6：进行降维变换")
        lower_xs = []
        for x in xs:
            lower_x = np.matmul(x, dimension_reduction_mat.transpose())
            lower_xs.append(lower_x)
        # self.lower_sample = lower_xs
        lower_xs = np.array(lower_xs).astype(np.float)  # 避免出现复数
        self.data = lower_xs
        # self.data = []
        # for lower_x in lower_xs:
        #     x = []
        #     for dim in lower_x:
        #         x.append(dim)
        #     self.data.append(np.array(x))
        # self.data = np.array(self.data)

# s = ReadMatFile('AR_120_14_50_45.mat').sample
# pca = PCA(sample=s, lower_dimension=1000)
# print(pca.lower_sample[0].shape)
