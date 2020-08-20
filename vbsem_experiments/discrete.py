from scipy.io import arff
import numpy as np
import pandas as pd

data_name = "asia"
missing_percentage = 0.2
data_types = "cccccccc"
i = 1

percentage_string = "0" + str(int(missing_percentage * 10))
base_path = "../vbsem_data/discrete/" + data_name + "/" + percentage_string + "/"
missing_data_path = base_path + data_name + "_" + percentage_string + "_" + str(i) + ".arff"
missing_data = arff.loadarff(missing_data_path)
missing_data = pd.DataFrame(missing_data[0])

print(missing_data.dtypes)

missing_data.replace(b'?', np.nan, inplace=True)
for col in missing_data:
    missing_data[col] = pd.to_numeric(missing_data[col])

print(missing_data.dtypes)

# Prepare GLFM data structure
missing_data_struct = dict()
missing_data_struct['X'] = missing_data.values  # Numpy form
missing_data_struct['C'] = data_types

check_nan = np.isnan(missing_data_struct['X'])