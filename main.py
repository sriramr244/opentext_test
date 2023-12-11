from dre_random.utils.common import import_and_validate_xml, parse_xml_to_dict
from dre_random.utils.common import read_yaml
from dre_random.components.build_list import gen_and_store_random_numbers
from dre_random.components.build_interval import create_and_store_intervals
import os
from constants import *
from pathlib import Path
from dre_random import logger


def main():
    config = read_yaml(CONFIG_PATH)
    params = read_yaml(PARAMS_PATH)

    i = 0
    while True:
        has_job_completed = True
        if len(os.listdir(config["job_input"]["root_dir"])) <= 0:
            logger.info(f">>>>>> Total {i-1} Jobs completed <<<<<<")
            break
        xml_file_path = os.path.join(
            config["job_input"]["root_dir"],
            Path(os.listdir(config["job_input"]["root_dir"])[0]),
        )
        try:
            logger.info(
                f">>>>>>Job {Path(os.listdir(config['job_input']['root_dir'])[0].split('.')[0])} started<<<<<<"
            )
            job_data = parse_xml_to_dict(
                import_and_validate_xml(
                    xml_file_path=xml_file_path,
                    xsd_file_path=os.path.join(
                        config["schema"]["root_dir"], params["SCHEMA_NAME"]
                    ),
                )
            )
            logger.info(f">>>>>>Job{i} validated<<<<<<")
        except Exception as e:
            logger.exception(e)
            has_job_completed = False
        if job_data["job_type"] == "build_list":
            try:
                gen_and_store_random_numbers(
                    seed=job_data["seed"],
                    length=job_data["list_length"],
                    file_path=os.path.join(
                        config["output_data"]["root_dir"], job_data["list_name"]
                    ),
                    chunk_size=params["CHUNK_SIZE"],
                )
                logger.info(f">>>>>>Job{i} list of random numbers generated<<<<<<")
            except Exception as e:
                logger.exception(e)
                has_job_completed = False

        else:
            try:
                create_and_store_intervals(
                    input_file_path=os.path.join(
                        config["output_data"]["root_dir"], job_data["list_name"]
                    ),
                    output_file_path=os.path.join(
                        config["output_data"]["root_dir"], job_data["interval_name"]
                    ),
                    min_val=job_data["min"],
                    max_val=job_data["max"],
                )
                logger.info(f">>>>>>Job{i} interval created<<<<<<")
            except Exception as e:
                logger.exception(e)
                has_job_completed = False
        if has_job_completed:
            i += 1
            os.remove(xml_file_path)


if __name__ == "__main__":
    main()
