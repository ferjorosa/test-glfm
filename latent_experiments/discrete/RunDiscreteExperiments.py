from latent_experiments.discrete import Exp_balance_scale
from latent_experiments.discrete import Exp_alarm
from latent_experiments.discrete import Exp_vote
from latent_experiments.discrete import Exp_breast_cancer
from latent_experiments.discrete import Exp_car_evaluation
from latent_experiments.discrete import Exp_coil_42
from latent_experiments.discrete import Exp_hayes_roth
from latent_experiments.discrete import Exp_hiv_test
from latent_experiments.discrete import Exp_house_building
from latent_experiments.discrete import Exp_mushroom
from latent_experiments.discrete import Exp_news_100
from latent_experiments.discrete import Exp_nursery
from latent_experiments.discrete import Exp_pascal_voc_2007
from latent_experiments.discrete import Exp_spect_heart
from latent_experiments.discrete import Exp_webkb_336

def main():
    run = 1
    n_folds = 10
    fold_log = True

    # exp = Exp_hiv_test.Exp_hiv_test("hiv_test")
    # exp.run(run, n_folds, fold_log)
    # 
    # exp = Exp_house_building.Exp_house_building("house_building")
    # exp.run(run, n_folds, fold_log)
    #
    # exp = Exp_hayes_roth.Exp_hayes_roth("hayes_roth")
    # exp.run(run, n_folds, fold_log)
    #
    # exp = Exp_balance_scale.Exp_balance_scale("balance_scale")
    # exp.run(run, n_folds, fold_log)

    # exp = Exp_car_evaluation.Exp_car_evaluation("car_evaluation")
    # exp.run(run, n_folds, fold_log)

    exp = Exp_nursery.Exp_nursery("nursery")
    exp.run(run, n_folds, fold_log)

    exp = Exp_breast_cancer.Exp_breast_cancer("breast_cancer")
    exp.run(run, n_folds, fold_log)

    exp = Exp_vote.Exp_vote("vote")
    exp.run(run, n_folds, fold_log)

    exp = Exp_mushroom.Exp_mushroom("mushroom")
    exp.run(run, n_folds, fold_log)

    exp = Exp_pascal_voc_2007.Exp_pascal_voc_2007("pascal_voc_2007")
    exp.run(run, n_folds, fold_log)

    exp = Exp_spect_heart.Exp_spect_heart("spect_heart")
    exp.run(run, n_folds, fold_log)

    exp = Exp_alarm.Exp_alarm("alarm")
    exp.run(run, n_folds, fold_log)

    # exp = Exp_coil_42.Exp_coil_42("coil_42")
    # exp.run(run, n_folds, fold_log)
    #
    # exp = Exp_news_100.Exp_news_100("news_100")
    # exp.run(run, n_folds, fold_log)
    #
    # exp = Exp_webkb_336.Exp_webkb_336("webkb_336")
    # exp.run(run, n_folds, fold_log)


if __name__ == "__main__":
    main()