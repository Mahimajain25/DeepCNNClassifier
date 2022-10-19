from deepClassifier import logger
from deepClassifier.components import DataIngestion
from deepClassifier.config import ConfigurationManager
from deepClassifier.constants import *


def main():
    config = ConfigurationManager(config_file_path=CONFIG_FILE_PATH,params_file_path=PARAMS_FILE_PATH)
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config= data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()

STAGE_NAME = "Data Ingestion stage"

if __name__ == "__main__":
   try:
       logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
       main()
       logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
   except Exception as e:
       logger.exception(e)
       raise e