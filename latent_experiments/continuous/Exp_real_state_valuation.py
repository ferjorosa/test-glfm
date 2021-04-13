import ContinuousExperiment


class Exp_real_state_valuation(ContinuousExperiment.ContinuousExperiment):

    def __init__(self, _data_name):
        ContinuousExperiment.ContinuousExperiment.__init__(self, _data_name)

    def run(self, run, n_folds, fold_log):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("---------------------- REAL_STATE_VALUATION ----------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")

        ContinuousExperiment.ContinuousExperiment.run(self, run, n_folds, fold_log)


def main():
    run = 1
    n_folds = 10

    data_name = "real_state_valuation"
    fold_log = True
    exp = Exp_real_state_valuation(data_name)
    exp.run(run, n_folds, fold_log)


if __name__ == "__main__":
    main()