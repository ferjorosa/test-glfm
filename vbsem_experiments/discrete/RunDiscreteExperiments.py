from vbsem_experiments.discrete import Exp_alarm
from vbsem_experiments.discrete import Exp_balance_scale
from vbsem_experiments.discrete import Exp_breast_cancer
from vbsem_experiments.discrete import Exp_car_evaluation
from vbsem_experiments.discrete import Exp_coil_42
from vbsem_experiments.discrete import Exp_hannover
from vbsem_experiments.discrete import Exp_hayes_roth
from vbsem_experiments.discrete import Exp_hiv_test
from vbsem_experiments.discrete import Exp_monks_1
from vbsem_experiments.discrete import Exp_monks_2
from vbsem_experiments.discrete import Exp_monks_3
from vbsem_experiments.discrete import Exp_mushroom
from vbsem_experiments.discrete import Exp_news_100
from vbsem_experiments.discrete import Exp_nursery
from vbsem_experiments.discrete import Exp_pascal_voc_2007
from vbsem_experiments.discrete import Exp_solar_flare
from vbsem_experiments.discrete import Exp_sommerville
from vbsem_experiments.discrete import Exp_spect_heart
from vbsem_experiments.discrete import Exp_vote
from vbsem_experiments.discrete import Exp_web_phishing
from vbsem_experiments.discrete import Exp_webkb_336
from vbsem_experiments.discrete import Exp_zoo


def main():
    n_runs = 5
    run_log = True

    for i in range(1, 7):
        missing_percentage = i / 10.0

        exp = Exp_alarm.Exp_alarm("alarm")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_balance_scale.Exp_balance_scale("balance_scale")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_breast_cancer.Exp_breast_cancer("breast_cancer")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_car_evaluation.Exp_car_evaluation("car_evaluation")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_coil_42.Exp_coil_42("coil_42")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_hannover.Exp_hannover("hannover")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_hayes_roth.Exp_hayes_roth("hayes_roth")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_hiv_test.Exp_hiv_test("hiv_test")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_monks_1.Exp_monks_1("monks_1")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_monks_2.Exp_monks_2("monks_2")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_monks_3.Exp_monks_3("monks_3")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_mushroom.Exp_mushroom("mushroom")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_news_100.Exp_news_100("news_100")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_nursery.Exp_nursery("nursery")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_pascal_voc_2007.Exp_pascal_voc_2007("pascal_voc_2007")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_solar_flare.Exp_solar_flare("solar_flare")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_sommerville.Exp_sommerville("sommerville")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_spect_heart.Exp_spect_heart("spect_heart")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_vote.Exp_vote("vote")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_web_phishing.Exp_web_phishing("web_phishing")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_webkb_336.Exp_webkb_336("webkb_336")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_zoo.Exp_zoo("zoo")
        exp.run(missing_percentage, n_runs, run_log)


if __name__ == "__main__":
    main()