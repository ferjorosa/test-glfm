import numpy as np
import pandas as pd
from scipy.io import arff


directory = "../vbsem_data/mixed/"
data_name = "iris"
percentage = 0.2
percentage_string = "0" + str(int(percentage * 10))
i = 1
file_name = data_name + "_" + percentage_string + "_" + str(i) + ".arff"
data_path = directory + data_name + "/" + percentage_string + "/" + file_name
data = arff.loadarff(data_path)
data = pd.DataFrame(data[0])
data.replace(b'?', np.nan, inplace=True)
