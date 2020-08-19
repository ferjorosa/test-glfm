from scipy.io import arff
import numpy as np
import pandas as pd
import time
from vbsem_experiments import EstimateMSE

import sys
import os
#sys.path.append('../../src/GLFMpython/')
root = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-3])
sys.path.append(os.path.join(root, 'src/GLFMpython/'))
import GLFM

missing_percentage = 0.2
data_name = "buddymove"
data_types = "gggggg"
i = 1

percentage_string = "0" + str(int(missing_percentage * 10))
base_path = "../../vbsem_data/continuous/" + data_name + "/" + percentage_string + "/"

# Load missing dataset
missing_data_path = base_path + data_name + "_" + percentage_string + "_" + str(i) + ".arff"
missing_data = arff.loadarff(missing_data_path)
missing_data = pd.DataFrame(missing_data[0])

str_data = missing_data.select_dtypes([np.object])
if str_data.empty == False:
    str_data = str_data.stack().str.decode('utf-8').unstack()
    for col in str_data:
        missing_data[col] = str_data[col]
missing_data.replace(b'?', np.nan, inplace=True)
missing_data.replace("?", np.nan, inplace=True)

# Prepare GLFM data structure
missing_data_struct = dict()
missing_data_struct['X'] = missing_data.values  # Numpy form
missing_data_struct['C'] = data_types

# Complete missing values with GLFM
init_time = time.time() * 1000
result = GLFM.complete(missing_data_struct)
end_time = time.time() * 1000
imputed_data = pd.DataFrame(result[0])

print end_time - init_time

# Load data without missing values
true_data_path = "../../vbsem_data/continuous/" + data_name + "/" + data_name + ".arff"
true_data = arff.loadarff(true_data_path)
true_data = pd.DataFrame(true_data[0])

# Estimate MSE of the imputed dataset
mse = EstimateMSE.mse(missing_data, imputed_data, true_data)
print mse

