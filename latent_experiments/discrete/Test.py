from scipy.io import arff
import numpy as np
import pandas as pd
import time
import json

import sys
import os
#sys.path.append('../../src/GLFMpython/')
root = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-3])
sys.path.append(os.path.join(root, 'src/GLFMpython/'))
import GLFM


# Notas: Tarda en ejecutarse unos 1100s
# El problema tiene pinta de ser similar al que ya arregle en su momento, no tiene bien implementado el tema
# de las categoricas.
#
# IndexError: index 3 is out of bounds for axis 0 with size 3
# El problema es que arreglar esto puede ser un lio, vamos a ver como se comporta con el resto de experimentos...

def main():

    i = 10
    data_name = "mushroom"
    data_types = generate_data_types(data_name)

    base_path = "../latent_data/discrete/" + data_name + "/10_folds/"

    train_data_path = base_path + data_name + "_" + str(i) + "_train.arff"
    test_data_path = base_path + data_name + "_" + str(i) + "_test.arff"

    # Load data
    train_data = arff.loadarff(train_data_path)
    train_data = pd.DataFrame(train_data[0])
    # Transform all column types to numeric (requirement of GLFM)
    for col in train_data:
        train_data[col] = train_data[col].astype("float64")
    train_data = train_data.values

    test_data = arff.loadarff(test_data_path)
    test_data = pd.DataFrame(test_data[0])
    # Transform all column types to numeric (requirement of GLFM)
    for col in test_data:
        test_data[col] = test_data[col].astype("float64")
    test_data = test_data.values

    # Prepare GLFM data structure
    test_data_struct = dict()
    test_data_struct['X'] = test_data  # Numpy form
    test_data_struct['C'] = data_types

    train_data_struct = dict()
    train_data_struct['X'] = train_data  # Numpy form
    train_data_struct['C'] = data_types

    ########### LEARN ############
    init_time = time.time() * 1000

    # Prepare GLFM init params
    params = dict()
    params = GLFM.init_default_params(train_data_struct, params)
    # Learn model
    hidden = GLFM.infer(train_data_struct, params=params)
    # Compute Test LL with my version of computeLL (see GLFM file for an explanation, but basically, it avoids
    # certain problems that are present in the original version, such as -Inf in the logarithm)
    test_ll = GLFM.compute_log_likelihood_2(test_data_struct['X'], test_data_struct['C'], hidden, params)
    test_ll = np.sum(test_ll)

    end_time = time.time() * 1000
    learning_time = end_time - init_time

def generate_data_types(data_name):
    data_path = "../latent_data/discrete/" + data_name + "/10_folds/" + data_name + "_1_train.arff"
    data = arff.loadarff(data_path)
    data = pd.DataFrame(data[0])

    s = ""
    for type in data.dtypes:
        if type.name.startswith("float"):
            s += "g"
        elif type.name == "object":
            s += "c"
    return s

if __name__ == '__main__':
    main()