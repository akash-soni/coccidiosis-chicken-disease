from cdisease.logging import logger
from cdisease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cdisease.pipeline.stage_02_prepare_base_mode import (
    PrepareBaseModelTrainingPipeline,
)

STAGE_NAME = "DATA_INGESTION_STAGE"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "BASE_MODEL_PREPERATION_STAGE"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
