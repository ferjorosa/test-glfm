from latent_experiments.continuous import Exp_100_plants
from latent_experiments.continuous import Exp_alcohol
from latent_experiments.continuous import Exp_buddymove
from latent_experiments.continuous import Exp_geo_music
from latent_experiments.continuous import Exp_glass
from latent_experiments.continuous import Exp_ilpd
from latent_experiments.continuous import Exp_ionosphere
from latent_experiments.continuous import Exp_iris
from latent_experiments.continuous import Exp_leaf
from latent_experiments.continuous import Exp_nba
from latent_experiments.continuous import Exp_vehicle
from latent_experiments.continuous import Exp_waveform
from latent_experiments.continuous import Exp_wdbc
from latent_experiments.continuous import Exp_wine
from latent_experiments.continuous import Exp_yeast


def main():
    run = 1
    n_folds = 10
    fold_log = True

    exp = Exp_iris.Exp_iris("iris")
    exp.run(run, n_folds, fold_log)

    exp = Exp_buddymove.Exp_buddymove("buddymove")
    exp.run(run, n_folds, fold_log)

    exp = Exp_yeast.Exp_yeast("yeast")
    exp.run(run, n_folds, fold_log)

    exp = Exp_glass.Exp_glass("glass")
    exp.run(run, n_folds, fold_log)

    exp = Exp_ilpd.Exp_ilpd("ilpd")
    exp.run(run, n_folds, fold_log)

    exp = Exp_alcohol.Exp_alcohol("alcohol")
    exp.run(run, n_folds, fold_log)

    exp = Exp_wine.Exp_wine("wine")
    exp.run(run, n_folds, fold_log)

    exp = Exp_leaf.Exp_leaf("leaf")
    exp.run(run, n_folds, fold_log)

    exp = Exp_nba.Exp_nba("nba")
    exp.run(run, n_folds, fold_log)

    exp = Exp_vehicle.Exp_vehicle("vehicle")
    exp.run(run, n_folds, fold_log)

    exp = Exp_wdbc.Exp_wdbc("wdbc")
    exp.run(run, n_folds, fold_log)

    exp = Exp_ionosphere.Exp_ionosphere("ionosphere")
    exp.run(run, n_folds, fold_log)

    exp = Exp_100_plants.Exp_100_plants("100_plants")
    exp.run(run, n_folds, fold_log)

    exp = Exp_waveform.Exp_waveform("waveform")
    exp.run(run, n_folds, fold_log)

    exp = Exp_geo_music.Exp_geo_music("geo_music")
    exp.run(run, n_folds, fold_log)


if __name__ == "__main__":
    main()