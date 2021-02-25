import ContinuousExperiment


class Exp_alcohol(ContinuousExperiment.ContinuousExperiment):

    def __init__(self, _data_name):
        ContinuousExperiment.ContinuousExperiment.__init__(self, _data_name)

    def run(self, run, n_folds, fold_log):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("----------------------------- ALCOHOL ----------------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")

        ContinuousExperiment.ContinuousExperiment.run(self, run, n_folds, fold_log)


def main():
    run = 1
    n_folds = 10

    data_name = "alcohol"
    fold_log = True
    exp = Exp_alcohol(data_name)
    exp.run(run, n_folds, fold_log)


if __name__ == "__main__":
    main()