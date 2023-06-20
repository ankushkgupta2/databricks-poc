import os 
import glob


class UtilityFunctions():
    def __init__(self):
        """
        """

    @staticmethod
    def call_submission(output_dir, meta_dir_name, lift_dir_name, sub_dir_name, batch_name, run_method):
        # initialize the checks class/methods
        output_checks = OutputChecks()

        # remove the previous submission files
        os.system (
            f"rm -rf {output_dir}/{sub_dir_name}"
        )
        assert not os.path.exists(f"{output_dir}/{sub_dir_name}")

        # call the submission entrypoint
        os.system (
            f"nextflow run main.nf -profile test,{run_method} -entry only_submission --submission_wait_time 2 --output_dir {output_dir} " + \
            f"--submission_only_meta {output_dir}/{meta_dir_name}/*/tsv_per_sample/ --submission_only_fasta {output_dir}/{lift_dir_name}/*/fasta/ " + \
            f"--submission_only_gff {output_dir}/{lift_dir_name}/*/liftoff/ --submission_output_dir {sub_dir_name} --batch_name {batch_name} " + \
            f"--submission_database all"
        )
        assert os.path.exists(f"{output_dir}/{sub_dir_name}")
    
    @staticmethod
    def read_file_lines(path_to_file):
        lines = open(glob.glob(path_to_file)[0], "r")
        lines = [x.strip() for x in lines]
        return lines
    
    @staticmethod
    def remove_files(directory_to_remove):
        os.system (
            f"rm -rf {directory_to_remove}"
        )
        assert not os.path.exists(f"{directory_to_remove}")
        