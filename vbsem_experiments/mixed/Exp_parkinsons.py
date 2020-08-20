import MixedExperiment


class Exp_parkinsons(MixedExperiment.MixedExperiment):

    def __init__(self, _data_name):
        MixedExperiment.MixedExperiment.__init__(self, _data_name)

    def run(self, missing_percentage, n_runs, run_log):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("--------------------------- PARKINSONS ---------------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")

        MixedExperiment.MixedExperiment.run(self, missing_percentage, n_runs, run_log)


def main():
    n_runs = 10
    missing_percentage = 0.2
    data_name = "parkinsons"
    run_log = True
    exp = Exp_parkinsons(data_name)
    exp.run(missing_percentage, n_runs, run_log)


if __name__ == "__main__":
    main()
