from cdisease.logging import logger
from cdisease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "DATA_INGESTION_STAGE"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
