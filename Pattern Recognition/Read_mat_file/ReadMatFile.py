import scipy.io as scio
import numpy as np
from PIL import Image
from scipy.spatial.distance import cdist
import os
import shutil
import random


class ReadMatFile:
    # 读取出向量
    def read_mat_file(self):
        result_data = []
        mat_data = scio.loadmat(self.file_path)['DAT']
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

    def __init__(self, file_path):
        self.file_path = file_path
        self.sample = self.read_mat_file()