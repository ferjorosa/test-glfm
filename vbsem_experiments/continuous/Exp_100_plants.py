import ContinuousExperiment


class Exp_Buddymove(ContinuousExperiment.ContinuousExperiment):

    def __init__(self, _data_name, _data_types):
        ContinuousExperiment.ContinuousExperiment.__init__(self, _data_name, _data_types)

    def run(self, missing_percentage, n_runs, run_log):
        print("\n------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("--------------------------- 100_PLANTS ---------------------------")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------\n")

        ContinuousExperiment.ContinuousExperiment.run(self, missing_percentage, n_runs, run_log)


def main():
    n_runs = 3
    missing_percentage = 0.2
    data_name = "buddymove"
    run_log = True
    exp = Exp_Buddymove(data_name, data_types())
    exp.run(missing_percentage, n_runs, run_log)

def data_types():
    return "ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"


if __name__ == "__main__":
    main()