# Cargamos el dataset
# Seleccionamos las columnas de tipo string
# Las pasamos a tipo categorico
# Iteramos por las categoricas y las sustituimos por sus cat.codes

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