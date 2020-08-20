import ContinuousExperiment


class Exp_waveform(ContinuousExperiment.ContinuousExperiment):

    def __init__(self, _data_name):
        ContinuousExperiment.ContinuousExperiment.__init__(self, _data_name)

    def run(self, missing_percentage, n_runs, run_log):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("---------------------------- WAVEFORM ----------------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")

        ContinuousExperiment.ContinuousExperiment.run(self, missing_percentage, n_runs, run_log)


def main():
    n_runs = 3
    missing_percentage = 0.2
    data_name = "waveform"
    run_log = True
    exp = Exp_waveform(data_name)
    exp.run(missing_percentage, n_runs, run_log)


if __name__ == "__main__":
    main()
