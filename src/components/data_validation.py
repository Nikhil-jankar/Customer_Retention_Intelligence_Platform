import sys
import pandas as pd

from src.config import ARTIFACT_DIR
from src.exception import CustomException
from src.logger import logger


class DataValidation:

    def __init__(self):
        self.train_path = ARTIFACT_DIR / "train.csv"

    def validate_dataset(self):

        try:

            logger.info("Starting Data Validation")

            df = pd.read_csv(self.train_path)

            # 1. Empty dataset
            if df.empty:
                raise Exception("Dataset is empty")

            logger.info("Dataset is not empty")

            # 2. Required Columns
            required_columns = [
                "gender",
                "SeniorCitizen",
                "Partner",
                "Dependents",
                "tenure",
                "PhoneService",
                "InternetService",
                "Contract",
                "MonthlyCharges",
                "TotalCharges",
                "Churn"
            ]

            missing_columns = []

            for col in required_columns:

                if col not in df.columns:
                    missing_columns.append(col)

            if len(missing_columns) > 0:

                raise Exception(
                    f"Missing Columns : {missing_columns}"
                )

            logger.info("All required columns are present")

            # 3. Duplicate Rows

            duplicates = df.duplicated().sum()

            logger.info(f"Duplicate Rows : {duplicates}")

            # 4. Missing Values

            missing = df.isnull().sum()

            logger.info("Missing Values Summary")

            logger.info(f"\n{missing}")

            logger.info("Data Validation Completed Successfully")

            return True

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)