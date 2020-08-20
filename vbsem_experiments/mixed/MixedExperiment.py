from scipy.io import arff
import numpy as np
import pandas as pd
import time
from vbsem_experiments import Estimate
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

    def run(self, missing_percentage, n_runs, run_log):
        percentage_string = "0" + str(int(missing_percentage * 10))
        base_path = "../../vbsem_data/mixed/" + self.data_name + "/" + percentage_string + "/"

        # Load true dataset (no missing values)
        true_data_path = "../../vbsem_data/mixed/" + self.data_name + "/" + self.data_name + ".arff"
        true_data = arff.loadarff(true_data_path)
        true_data = pd.DataFrame(true_data[0])

        # Prepare result data structures (to export them as JSON)
        results = {}
        runs = {}
        avg_learning_time = 0
        avg_mse = 0
        avg_accuracy = 0

        # Load missing data and impute its missing values with GLFM, then estimate its mean squared error
        results_path = "../../vbsem_results/mixed/" + self.data_name + "/"
        for i in range(1, n_runs + 1):

            # Load missing dataset
            missing_data_path = base_path + self.data_name + "_" + percentage_string + "_" + str(i) + ".arff"
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
            missing_data_struct['C'] = self.data_types

            # Complete missing values with GLFM
            init_time = time.time() * 1000
            result = GLFM.complete(missing_data_struct)
            end_time = time.time() * 1000
            imputed_data = pd.DataFrame(result[0])

            # Store the MSE, the accuracy and the learning time
            accuracy = Estimate.accuracy(missing_data.select_dtypes([np.object]),
                                         imputed_data.select_dtypes([np.object]),
                                         true_data.select_dtypes([np.object]))
            mse = Estimate.mse(missing_data.select_dtypes(['float16', 'float32', 'float64']),
                               imputed_data.select_dtypes(['float16', 'float32', 'float64']),
                               true_data.select_dtypes(['float16', 'float32', 'float64']))
            learning_time = end_time - init_time

            run_result = {"mse": mse, "accuracy": accuracy, "learning_time": learning_time}

            runs["run_" + str(i)] = run_result
            avg_learning_time = avg_learning_time + learning_time
            avg_mse = avg_mse + mse
            avg_accuracy = avg_accuracy + accuracy

            if run_log:
                print("----------------------------------------")
                print("Run (" + str(i) + "): ")
                print("MSE: " + str(mse))
                print("Accuracy: " + str(accuracy))
                print("Learning time: " + str(learning_time))

        # Generate the average results and store them in the dictionary, then store them in a JSON file
        avg_mse = avg_mse / n_runs
        avg_accuracy = avg_accuracy / n_runs
        avg_learning_time = avg_learning_time / n_runs / 1000  # in seconds
        results["average_mse"] = avg_mse
        results["average_accuracy"] = avg_accuracy
        results["average_learning_time"] = avg_learning_time
        results["runs"] = runs
        self.store_json(results, results_path, percentage_string)

        print("----------------------------------------")
        print("----------------------------------------")
        print("Average MSE: " + str(avg_mse))
        print("Average Accuracy: " + str(avg_accuracy))
        print("Average learning time: " + str(avg_learning_time))


    def store_json(self, results, path, percentage_string):
        if not os.path.exists(path):
            os.makedirs(path)
        if os.path.isfile(path + self.data_name + "_" + percentage_string + "_results_GLFM.json"):
            os.remove(path + self.data_name + "_" + percentage_string + "_results_GLFM.json")
            with open(path + self.data_name + "_" + percentage_string + "_results_GLFM.json", 'w') as fp:
                json.dump(results, fp, sort_keys=True, indent=4)
        else:
            with open(path + self.data_name + "_" + percentage_string + "_results_GLFM.json", 'w') as fp:
                json.dump(results, fp, sort_keys=True, indent=4)


def data_types(data_name):
    data_path = "../../vbsem_data/mixed/" + data_name + "/" + data_name + ".arff"
    data = arff.loadarff(data_path)
    data = pd.DataFrame(data[0])

    s = ""
    for type in data.dtypes:
        if type.name.startswith("float"):
            s += "g"
        elif type.name == "object":
            s += "c"
    return s
