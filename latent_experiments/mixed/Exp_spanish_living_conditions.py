import MixedExperiment


class Exp_spanish_living_conditions(MixedExperiment.MixedExperiment):

    def __init__(self, _data_name):
        MixedExperiment.MixedExperiment.__init__(self, _data_name)

    def run(self, run, n_folds, fold_log):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("-------------------- SPANISH_LIVING_CONDITIONS -------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")

        MixedExperiment.MixedExperiment.run(self, run, n_folds, fold_log)


def main():
    run = 1
    n_folds = 10
    
    # It requires numeric format to work with GLFM
    data_name = "spanish_living_conditions_numeric"
    fold_log = True
    exp = Exp_spanish_living_conditions(data_name)
    exp.run(run, n_folds, fold_log)


if __name__ == "__main__":
    main()