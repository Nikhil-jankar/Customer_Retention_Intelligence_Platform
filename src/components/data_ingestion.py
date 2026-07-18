import os
import sys
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

from src.config import ARTIFACT_DIR, RAW_DATA_DIR
from src.exception import CustomException
from src.logger import logger


@dataclass
class DataIngestionConfig:

    train_data_path = ARTIFACT_DIR / "train.csv"

    test_data_path = ARTIFACT_DIR / "test.csv"

    raw_data_path = ARTIFACT_DIR / "raw.csv"
    
    
class DataIngestion:

    def __init__(self):

        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):

        logger.info("Entered Data Ingestion Component")

        try:

            dataset_path = RAW_DATA_DIR / "telco_customer_churn.csv"

            logger.info(f"Reading dataset from {dataset_path}")

            df = pd.read_csv(dataset_path)

            logger.info("Dataset loaded successfully")

            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True,
            )

            logger.info("Raw dataset saved into artifacts")

            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42,
                stratify=df["Churn"],
            )

            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True,
            )

            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True,
            )

            logger.info("Train/Test split completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)