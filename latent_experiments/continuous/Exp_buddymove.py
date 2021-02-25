import ContinuousExperiment


class Exp_buddymove(ContinuousExperiment.ContinuousExperiment):

    def __init__(self, _data_name):
        ContinuousExperiment.ContinuousExperiment.__init__(self, _data_name)

    def run(self, run, n_folds, fold_log):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("---------------------------- BUDDYMOVE ---------------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")

        ContinuousExperiment.ContinuousExperiment.run(self, run, n_folds, fold_log)


def main():
    run = 1
    n_folds = 1

    data_name = "buddymove"
    fold_log = True
    exp = Exp_buddymove(data_name)
    exp.run(run, n_folds, fold_log)


if __name__ == "__main__":
    main()