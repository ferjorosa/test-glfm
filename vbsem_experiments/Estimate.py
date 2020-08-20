from pandas import DataFrame
from scipy.stats import multivariate_normal
import numpy as np

"""
The purpose of this script is...
"""


def mse(missing_data, imputed_data, true_data):
    missing_count = 0
    sq_error = 0
    for i in range(0, imputed_data.shape[0]):
        for j in range(0, imputed_data.shape[1]):
            if np.isnan(missing_data.iloc[i][j]):
                missing_count = missing_count + 1
                sq_error += np.power(imputed_data.iloc[i][j] - true_data.iloc[i][j], 2)

    return sq_error / missing_count


def accuracy(missing_data, imputed_data, true_data):
    missing_count = 0
    right_count = 0
    for i in range(0, imputed_data.shape[0]):
        for j in range(0, imputed_data.shape[1]):
            if np.isnan(missing_data.iloc[i][j]):
                missing_count = missing_count + 1
                if imputed_data.iloc[i][j] == true_data.iloc[i][j]:
                    right_count = right_count + 1

    return right_count / missing_count
