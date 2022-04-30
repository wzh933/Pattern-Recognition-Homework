import scipy.io as scio
import numpy as np
from PIL import Image
from scipy.spatial.distance import cdist
import os
import shutil
import random


class K_means:

    # 欧式距离
    @staticmethod
    def euclidean_distance(x1, x2):
        return np.linalg.norm(x1 - x2)

    # 马氏距离
    def mahalanobis_distance(self, x1, x2):
        # X = sample[0]  # 将样本中所有向量横向拼接
        # for i in range(1, len(sample)):
        #     X = np.hstack((X, sample[i]))
        # sigma = np.cov(X)  # sigma是协方差矩阵
        # sigma_1 = np.linalg.inv(sigma)  # 对协方差矩阵求逆
        delta = x1 - x2
        dis = np.matmul(np.matmul(delta.transpose(), self.sigma_1), delta)
        # return np.sqrt(dis[0, 0])
        return dis[0, 0]

    # 曼哈顿距离
    @staticmethod
    def L1_distance(x1, x2):
        # return sum(abs(x1 - x2))[0, 0]

        return sum(map(lambda i, j: abs(i - j), x1, x2))[0, 0]

    # mat文件转换为bmp位图
    @staticmethod
    def Mat2Img(mat_data):
        mat_data = mat_data * 255
        new_img = Image.fromarray(mat_data.astype(np.uint8))
        return new_img

    def __init__(self, sample, k, iterate_nums, metric='euclidean', res_file_path='Euclidean_Res_Image'):
        xs = sample  # xs是样本集
        if metric == 'mahalanobis':  # 只有在求马氏距离时才会需要进行协方差矩阵的计算
            X = xs[0]  # 将样本中所有向量横向拼接
            for i in range(1, len(xs)):
                X = np.hstack((X, xs[i]))
            sigma = np.cov(X)  # sigma是协方差矩阵
            self.sigma_1 = np.linalg.inv(sigma)  # 对协方差矩阵求逆
        # 清除先前生成结果
        if os.path.exists(res_file_path):
            shutil.rmtree(res_file_path)
        os.mkdir(res_file_path)
        # 创建k个文件目录以存放后续结果
        path = res_file_path + '/'
        for i in range(k):
            os.mkdir(path + 'Image' + str(i))

        # step1：随机选取k个样本作为初始样本中心点
        orig_means = random.sample(sample, k)

        # step2：创建k个类别簇
        k_closures = [[] for i in range(k)]

        # step3：迭代求解
        for tot in range(iterate_nums):
            if (tot + 1) % 100 == 0:
                print("这是第" + str(tot + 1) + "次迭代")
            # print("这是第" + str(tot + 1) + "次迭代")
            # step3-1：对所有样本点进行分类
            for i in range(k):  # 要挨个清空之前的聚类结果
                k_closures[i].clear()
            for x in xs:
                dis_list = []  # 创建距离列表，里面装的是x与k个样本中心点的距离
                # print('start')
                for x_mean in orig_means:
                    if metric == 'euclidean':  # 欧氏距离
                        dis_list.append(self.euclidean_distance(x, x_mean))
                    elif metric == 'mahalanobis':  # 马氏距离
                        dis_list.append(self.mahalanobis_distance(x, x_mean))
                    elif metric == 'L1':  # 曼哈顿距离
                        dis_list.append(self.L1_distance(x, x_mean))
                # print('end')
                label = np.argmin(dis_list)  # 选择与x距离最近的类别为x的类别
                k_closures[label].append(x)  # 将x加入label类簇中
            # step3-2：重新计算各类簇中心点
            for label in range(k):
                orig_means[label] = sum(k_closures[label]) / len(k_closures[label])

        # step4：记录聚类结果
        for label in range(len(k_closures)):
            for cnt in range(len(k_closures[label])):
                Img_vector = k_closures[label][cnt]
                Img_mat = np.reshape(Img_vector, [80, 100])
                new_Img = self.Mat2Img(Img_mat)
                new_Img.save(path + 'Image' + str(label) + '/' + 'Image' + str(cnt) + '.bmp')


# 读取出向量
def read_mat_file(file_path):
    result_data = []
    mat_data = scio.loadmat(file_path)['DAT']
    row = len(mat_data[0])
    col = len(mat_data[0][0])
    for r in range(row):
        for c in range(col):
            x = []
            for data in mat_data:
                x.append(data[r][c])
            x = np.matrix(x).transpose()
            result_data.append(x)
    return result_data


# 输入样本
s = read_mat_file('Yale_15_11_100_80.mat')
km = K_means(sample=s, k=15, iterate_nums=1000)  # 欧式距离
# km = K_means(sample=s, k=15, iterate_nums=1000, metric='mahalanobis', res_file_path='Mahalanobis_Res_Image')  # 马氏距离
# km = K_means(sample=s, k=15, iterate_nums=1000, metric='L1', res_file_path='L1_Res_Image')  # 曼哈顿距离


# ----------------------------这是显示原始数据集的代码-------------------------------------------#
# def Mat2Img(mat_data):
#     mat_data = mat_data * 255
#     new_img = Image.fromarray(mat_data.astype(np.uint8))
#     return new_img
#
#
# mat_path = r'Yale_15_11_100_80.mat'
# mat_data = scio.loadmat(mat_path)['DAT']
#
# if os.path.exists('Orig_Image'):
#     shutil.rmtree('Orig_Image')
# os.mkdir('Orig_Image')
#
# for i in range(15):
#     os.mkdir('Orig_Image/Image' + str(i))
# # 显示165张图片
# for row in range(11):
#     for col in range(15):
#         img = []
#         for data in mat_data:
#             img.append(data[row][col])
#         img = np.array(img)
#         img = np.reshape(img, [80, 100])
#         new_img = Mat2Img(img)
#         new_img.save('Orig_Image/Image' + str(col) + '/Image' + str(row) + '.bmp')
# -----------------------------------------------------------------------------------------#