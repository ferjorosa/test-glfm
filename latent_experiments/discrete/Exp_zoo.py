import DiscreteExperiment


class Exp_zoo(DiscreteExperiment.DiscreteExperiment):

    def __init__(self, _data_name):
        DiscreteExperiment.DiscreteExperiment.__init__(self, _data_name)

    def run(self, run, n_folds, fold_log):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("------------------------------- ZOO ------------------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")

        DiscreteExperiment.DiscreteExperiment.run(self, run, n_folds, fold_log)


def main():
    run = 1
    n_folds = 10

    data_name = "zoo"
    fold_log = True
    exp = Exp_zoo(data_name)
    exp.run(run, n_folds, fold_log)


if __name__ == "__main__":
    main()