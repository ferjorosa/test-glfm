import MixedExperiment


class Exp_breast_cancer_coimbra(MixedExperiment.MixedExperiment):

    def __init__(self, _data_name):
        MixedExperiment.MixedExperiment.__init__(self, _data_name)

    def run(self, missing_percentage, n_runs, run_log):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("--------------------- BREAST_CANCER_COIMBRA ----------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")
        print("Missing percentage: " + str(missing_percentage) + "\n")

        MixedExperiment.MixedExperiment.run(self, missing_percentage, n_runs, run_log)


def main():
    n_runs = 5
    data_name = "breast_cancer_coimbra"
    run_log = True
    exp = Exp_breast_cancer_coimbra(data_name)

    for i in range(1, 6):
        missing_percentage = i / 10.0
        exp.run(missing_percentage, n_runs, run_log)


if __name__ == "__main__":
    main()
