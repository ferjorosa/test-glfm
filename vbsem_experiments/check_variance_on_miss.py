from scipy.io import arff
import numpy as np
import pandas as pd
import os

data_name = "iris"
missing_percentage = 0.2
i = 1
percentage_string = "0" + str(int(missing_percentage * 10))

directory = "../vbsem_data/mixed/"
data_names = os.listdir(directory)

for data_name in data_names:
    print("\n-------------------")
    print(data_name)
    for percentage in range(1, 7, 1):
        percentage = percentage / 10.0
        percentage_string = "0" + str(int(percentage * 10))
        print(percentage_string)
        for i in range(1, 11, 1):
            file_name = data_name + "_" + percentage_string + "_" + str(i) + ".arff"
            data_path = directory + data_name + "/" + percentage_string + "/" + file_name
            data = arff.loadarff(data_path)
            data = pd.DataFrame(data[0])
            data.replace(b'?', np.nan, inplace=True)
            for col in data:
                data[col] = pd.to_numeric(data[col])
            if 0.0 in data.var().values:
                print("MISSING COLUMN IN: " + file_name)

print "\n\n ------------------------- FINISHED ---------------------------"




