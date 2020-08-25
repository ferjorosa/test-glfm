from vbsem_experiments.mixed import Exp_abalone
from vbsem_experiments.mixed import Exp_autos
from vbsem_experiments.mixed import Exp_blood_transfusion
from vbsem_experiments.mixed import Exp_breast_cancer_coimbra
from vbsem_experiments.mixed import Exp_cpu
from vbsem_experiments.mixed import Exp_cylinder_bands
from vbsem_experiments.mixed import Exp_ecoli
from vbsem_experiments.mixed import Exp_forest_fires
from vbsem_experiments.mixed import Exp_glass
from vbsem_experiments.mixed import Exp_haberman
from vbsem_experiments.mixed import Exp_ionosphere
from vbsem_experiments.mixed import Exp_iris
from vbsem_experiments.mixed import Exp_musk
from vbsem_experiments.mixed import Exp_parkinsons
from vbsem_experiments.mixed import Exp_planning_relax
from vbsem_experiments.mixed import Exp_qsar_biodeg
from vbsem_experiments.mixed import Exp_seeds
from vbsem_experiments.mixed import Exp_segment
from vbsem_experiments.mixed import Exp_thoracic_surgery
from vbsem_experiments.mixed import Exp_thyroid
from vbsem_experiments.mixed import Exp_user_knowledge
from vbsem_experiments.mixed import Exp_vehicle
from vbsem_experiments.mixed import Exp_vertebral
from vbsem_experiments.mixed import Exp_wdbc
from vbsem_experiments.mixed import Exp_wine
from vbsem_experiments.mixed import Exp_yeast


def main():
    n_runs = 5
    run_log = True

    for i in range(1, 7):
        missing_percentage = i / 10.0

        exp = Exp_abalone.Exp_abalone("abalone")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_autos.Exp_autos("autos")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_blood_transfusion.Exp_blood_transfusion("blood_transfusion")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_breast_cancer_coimbra.Exp_breast_cancer_coimbra("breast_cancer_coimbra")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_cpu.Exp_cpu("cpu")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_cylinder_bands.Exp_cylinder_bands("cylinder_bands")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_ecoli.Exp_ecoli("ecoli")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_forest_fires.Exp_forest_fires("forest_fires")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_glass.Exp_glass("glass")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_haberman.Exp_haberman("haberman")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_ionosphere.Exp_ionosphere("ionosphere")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_iris.Exp_iris("iris")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_musk.Exp_musk("musk")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_parkinsons.Exp_parkinsons("parkinsons")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_planning_relax.Exp_planning_relax("planning_relax")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_qsar_biodeg.Exp_qsar_biodeg("qsar_biodeg")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_seeds.Exp_seeds("seeds")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_segment.Exp_segment("segment")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_thoracic_surgery.Exp_thoracic_surgery("thoracic_surgery")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_thyroid.Exp_thyroid("thyroid")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_user_knowledge.Exp_user_knowledge("user_knowledge")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_vehicle.Exp_vehicle("vehicle")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_vertebral.Exp_vertebral("vertebral")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_wdbc.Exp_wdbc("wdbc")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_wine.Exp_wine("wine")
        exp.run(missing_percentage, n_runs, run_log)

        exp = Exp_yeast.Exp_yeast("yeast")
        exp.run(missing_percentage, n_runs, run_log)


if __name__ == "__main__":
    main()
