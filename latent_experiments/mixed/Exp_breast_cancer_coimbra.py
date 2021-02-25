import MixedExperiment


class Exp_breast_cancer_coimbra(MixedExperiment.MixedExperiment):

    def __init__(self, _data_name):
        MixedExperiment.MixedExperiment.__init__(self, _data_name)

    def run(self, run, n_folds, fold_log):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("---------------------- BREAST_CANCER_COIMBRA ---------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")

        MixedExperiment.MixedExperiment.run(self, run, n_folds, fold_log)


def main():
    run = 1
    n_folds = 10

    data_name = "breast_cancer_coimbra"
    fold_log = True
    exp = Exp_breast_cancer_coimbra(data_name)
    exp.run(run, n_folds, fold_log)


if __name__ == "__main__":
    main()