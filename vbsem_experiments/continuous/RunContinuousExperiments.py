from vbsem_experiments.continuous import Exp_100_plants
from vbsem_experiments.continuous import Exp_buddymove
from vbsem_experiments.continuous import Exp_geo_music
from vbsem_experiments.continuous import Exp_leaf
from vbsem_experiments.continuous import Exp_ml_prove
from vbsem_experiments.continuous import Exp_mobile_ksd_2016
from vbsem_experiments.continuous import Exp_online_news_popularity
from vbsem_experiments.continuous import Exp_qsar_fish_toxicity
from vbsem_experiments.continuous import Exp_qsar_aqua_toxicity
from vbsem_experiments.continuous import Exp_res_building
from vbsem_experiments.continuous import Exp_real_state_valuation
from vbsem_experiments.continuous import Exp_superconduct
from vbsem_experiments.continuous import Exp_travel_reviews
from vbsem_experiments.continuous import Exp_waveform
from vbsem_experiments.continuous import Exp_wine_quality_white


def main():
    missing_percentage = 0.1
    n_runs = 10
    run_log = True

    exp = Exp_buddymove.Exp_buddymove("buddymove")
    exp.run(missing_percentage, n_runs, run_log)

    exp = Exp_geo_music.Exp_geo_music("geo_music")
    exp.run(missing_percentage, n_runs, run_log)

    exp = Exp_leaf.Exp_leaf("leaf")
    exp.run(missing_percentage, n_runs, run_log)

    exp = Exp_ml_prove.Exp_ml_prove("ml_prove")
    exp.run(missing_percentage, n_runs, run_log)

    exp = Exp_mobile_ksd_2016.Exp_mobile_ksd_2016("mobile_ksd_2016")
    exp.run(missing_percentage, n_runs, run_log)

    exp = Exp_online_news_popularity.Exp_online_news_popularity("online_news_popularity")
    exp.run(missing_percentage, n_runs, run_log)

    exp = Exp_qsar_aqua_toxicity.Exp_qsar_aqua_toxicity("qsar_aqua_toxicity")
    exp.run(missing_percentage, n_runs, run_log)

    exp = Exp_qsar_fish_toxicity.Exp_qsar_fish_toxicity("qsar_fish_toxicity")
    exp.run(missing_percentage, n_runs, run_log)

    exp = Exp_real_state_valuation.Exp_real_state_valuation("real_state_valuation")
    exp.run(missing_percentage, n_runs, run_log)

    exp = Exp_res_building.Exp_res_building("res_building")
    exp.run(missing_percentage, n_runs, run_log)

    exp = Exp_superconduct.Exp_superconduct("superconduct")
    exp.run(missing_percentage, n_runs, run_log)

    exp = Exp_travel_reviews.Exp_travel_reviews("travel_reviews")
    exp.run(missing_percentage, n_runs, run_log)

    exp = Exp_waveform.Exp_waveform("waveform")
    exp.run(missing_percentage, n_runs, run_log)

    exp = Exp_wine_quality_white.Exp_wine_quality_white("wine_quality_white")
    exp.run(missing_percentage, n_runs, run_log)


if __name__ == "__main__":
    main()