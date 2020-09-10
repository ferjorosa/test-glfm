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
            if np.isnan(missing_data.iloc[i, j]):
                missing_count = missing_count + 1
                sq_error += np.power(imputed_data.iloc[i, j] - true_data.iloc[i, j], 2)

    if missing_count == 0:
        return 0.0

    return sq_error / missing_count


# See: https://en.wikipedia.org/wiki/Root-mean-square_deviation#Normalized_root-mean-square_deviation
def nrmse(missing_data, imputed_data, true_data):
    total_missing_count = 0.0
    normalized_error = 0.0
    for j in range(0, imputed_data.shape[1]):
        attribute_missing_count = 0.0
        attribute_error = 0.0
        for i in range(0, imputed_data.shape[0]):
            if np.isnan(missing_data.iloc[i, j]):
                total_missing_count += 1
                attribute_missing_count += 1
                attribute_error += np.power(imputed_data.iloc[i, j] - true_data.iloc[i, j], 2)
        attribute_error = np.sqrt(attribute_error / attribute_missing_count)
        normalized_error += attribute_error / (true_data.iloc[:, j].max() - true_data.iloc[:, j].min())

    if total_missing_count == 0:
        return 0.0

    return normalized_error / true_data.shape[1]


def accuracy(missing_data, imputed_data, true_data):
    missing_count = 0.0
    right_count = 0.0
    for i in range(0, imputed_data.shape[0]):
        for j in range(0, imputed_data.shape[1]):
            if np.isnan(missing_data.iloc[i, j]):
                missing_count = missing_count + 1
                if imputed_data.iloc[i, j] == true_data.iloc[i, j]:
                    right_count = right_count + 1

    if missing_count == 0:
        return 1.0

    return right_count / missing_count


def avg_error(missing_data, imputed_data, true_data, discrete_cols, continuous_cols):
    normalized_error = 0.0

    # Continuous attributes (NRMSE)
    continuous_imputed_data = imputed_data[continuous_cols]
    continuous_true_data = true_data[continuous_cols]
    continuous_missing_data = missing_data[continuous_cols]

    for j in range(0, continuous_imputed_data.shape[1]):
        attribute_missing_count = 0.0
        attribute_error = 0.0
        for i in range(0, continuous_imputed_data.shape[0]):
            if np.isnan(continuous_missing_data.iloc[i, j]):
                attribute_missing_count += 1
                attribute_error += np.power(continuous_imputed_data.iloc[i, j] - continuous_true_data.iloc[i, j], 2)
        attribute_error = np.sqrt(attribute_error / attribute_missing_count)
        normalized_error += attribute_error / (continuous_true_data.iloc[:, j].max() - continuous_true_data.iloc[:, j].min())

    # Discrete attributes (Accuracy error)
    discrete_imputed_data = imputed_data[discrete_cols]
    discrete_true_data = true_data[discrete_cols]
    discrete_missing_data = missing_data[discrete_cols]

    for j in range(0, discrete_imputed_data.shape[1]):
        attribute_missing_count = 0.0
        attribute_missing_wrong = 0.0
        for i in range(0, discrete_imputed_data.shape[0]):
            if np.isnan(discrete_missing_data.iloc[i, j]):
                attribute_missing_count += 1
                if discrete_imputed_data.iloc[i, j] != discrete_true_data.iloc[i, j]:
                    attribute_missing_wrong += 1
        attribute_error = 0.0
        if attribute_missing_count > 0:
            attribute_error = attribute_missing_wrong / attribute_missing_count
        normalized_error += attribute_error

    return normalized_error / true_data.shape[1]