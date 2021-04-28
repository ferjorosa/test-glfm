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


class MixedExperiment:

    def __init__(self, data_name):
        self.data_name = data_name
        self.data_types = data_types(data_name)

    def run(self, run, n_folds, fold_log):
        base_path = "../../latent_data/mixed/" + self.data_name + "/10_folds/"
        results_path = "../../latent_results/run_" + str(run) + "/mixed/" + self.data_name + "/" + \
                       str(n_folds) + "_folds/GLFM/"

        print("\n========================")
        print("GLFM")
        print("========================")

        results = {}
        folds = {}
        avg_learning_time = 0
        avg_test_ll = 0

        # Prepare folds' data
        for i in range(9, n_folds+1):
            train_data_path = base_path + self.data_name + "_" + str(i) + "_train.arff"
            test_data_path = base_path + self.data_name + "_" + str(i) + "_test.arff"

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
            test_data_struct['C'] = self.data_types

            train_data_struct = dict()
            train_data_struct['X'] = train_data  # Numpy form
            train_data_struct['C'] = self.data_types

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

            # Average results
            fold_result = {"test_LL": test_ll, "learning_time": learning_time}

            folds["fold_" + str(i)] = fold_result
            avg_learning_time = avg_learning_time + learning_time
            avg_test_ll = avg_test_ll + test_ll

            if fold_log:
                print("----------------------------------------")
                print("Fold (" + str(i) + "): ")
                print("Test LL: " + str(test_ll))
                print("Learning time: " + str(learning_time))

        # Generate the average results and store them in the dictionary, then store them in a JSON file
        avg_test_ll = avg_test_ll / n_folds
        avg_learning_time = avg_learning_time / n_folds / 1000  # in seconds
        results["average_test_LL"] = avg_test_ll
        results["average_learning_time"] = avg_learning_time
        results["folds"] = folds
        self.store_json(results, results_path)

        print("----------------------------------------")
        print("----------------------------------------")
        print("Average Test LL: " + str(avg_test_ll))
        print("Average learning time: " + str(avg_learning_time))

    def store_json(self, results, path):
        if not os.path.exists(path):
            os.makedirs(path)
        if os.path.isfile(path + self.data_name + "_results_GLFM.json"):
            os.remove(path + self.data_name + "_results_GLFM.json")
            with open(path + self.data_name + "_results_GLFM.json", 'w') as fp:
                json.dump(results, fp, sort_keys=True, indent=4)
        else:
            with open(path + self.data_name + "_results_GLFM.json", 'w') as fp:
                json.dump(results, fp, sort_keys=True, indent=4)

        return 0


def data_types(data_name):
    data_path = "../../latent_data/mixed/" + data_name + "/10_folds/" + data_name + "_1_train.arff"
    data = arff.loadarff(data_path)
    data = pd.DataFrame(data[0])

    s = ""
    for type in data.dtypes:
        if type.name.startswith("float"):
            s += "g"
        elif type.name == "object":
            s += "c"
    return s