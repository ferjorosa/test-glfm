import ContinuousExperiment


class Exp_wdbc(ContinuousExperiment.ContinuousExperiment):

    def __init__(self, _data_name):
        ContinuousExperiment.ContinuousExperiment.__init__(self, _data_name)

    def run(self, missing_percentage, n_runs, run_log):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("------------------------------ WDBC ------------------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")
        print("Missing percentage: " + str(missing_percentage) + "\n")

        ContinuousExperiment.ContinuousExperiment.run(self, missing_percentage, n_runs, run_log)


def main():
    data_name = "wdbc"
    exp = Exp_wdbc(data_name)
    n_runs = 5
    run_log = True

    for i in range(1, 6):
        missing_percentage = i / 10.0
        exp.run(missing_percentage, n_runs, run_log)


if __name__ == "__main__":
    main()
