import DiscreteExperiment


class Exp_monks_3(DiscreteExperiment.DiscreteExperiment):

    def __init__(self, _data_name):
        DiscreteExperiment.DiscreteExperiment.__init__(self, _data_name)

    def run(self, missing_percentage, n_runs, run_log):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("---------------------------- MONKS_3 -----------------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")

        DiscreteExperiment.DiscreteExperiment.run(self, missing_percentage, n_runs, run_log)


def main():
    n_runs = 10
    missing_percentage = 0.2
    data_name = "monks_3"
    run_log = True
    exp = Exp_monks_3(data_name)
    exp.run(missing_percentage, n_runs, run_log)


if __name__ == "__main__":
    main()
