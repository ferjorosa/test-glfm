import DiscreteExperiment


class Exp_spect_heart(DiscreteExperiment.DiscreteExperiment):

    def __init__(self, _data_name):
        DiscreteExperiment.DiscreteExperiment.__init__(self, _data_name)

    def run(self, missing_percentage, n_runs, run_log):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("-------------------------- SPECT_HEART ---------------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")
        print("Missing percentage: " + str(missing_percentage) + "\n")

        DiscreteExperiment.DiscreteExperiment.run(self, missing_percentage, n_runs, run_log)


def main():
    n_runs = 5
    data_name = "spect_heart"
    run_log = True
    exp = Exp_spect_heart(data_name)

    for i in range(1, 6):
        missing_percentage = i / 10.0
        exp.run(missing_percentage, n_runs, run_log)


if __name__ == "__main__":
    main()
