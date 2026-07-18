import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.config import ARTIFACT_DIR
from src.exception import CustomException
from src.logger import logger
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = ARTIFACT_DIR / "preprocessor.pkl"


class DataTransformation:

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        Creates preprocessing pipeline.
        """

        try:

            numeric_features = [
                "tenure",
                "MonthlyCharges",
                "TotalCharges"
            ]

            categorical_features = [
                "gender",
                "SeniorCitizen",
                "Partner",
                "Dependents",
                "PhoneService",
                "MultipleLines",
                "InternetService",
                "OnlineSecurity",
                "OnlineBackup",
                "DeviceProtection",
                "TechSupport",
                "StreamingTV",
                "StreamingMovies",
                "Contract",
                "PaperlessBilling",
                "PaymentMethod"
            ]

            logger.info("Creating Numerical Pipeline")

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            logger.info("Creating Categorical Pipeline")

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    (
                        "one_hot_encoder",
                        OneHotEncoder(handle_unknown="ignore")
                    )
                ]
            )

            logger.info("Combining Pipelines")

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, numeric_features),
                    ("cat_pipeline", cat_pipeline, categorical_features)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):

        try:

            logger.info("Reading Train and Test Data")

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logger.info("Fixing blank spaces in TotalCharges column")
            train_df['TotalCharges'] = pd.to_numeric(train_df['TotalCharges'], errors='coerce')
            test_df['TotalCharges'] = pd.to_numeric(test_df['TotalCharges'], errors='coerce')

            preprocessing_obj = self.get_data_transformer_object()

            target_column = "Churn"

            logger.info("Splitting Input Features and Target")

            input_feature_train_df = train_df.drop(columns=[target_column])

            target_feature_train_df = train_df[target_column]

            input_feature_test_df = test_df.drop(columns=[target_column])

            target_feature_test_df = test_df[target_column]

            logger.info("Applying Preprocessing")

            input_feature_train_arr = preprocessing_obj.fit_transform(
                input_feature_train_df
            )

            input_feature_test_arr = preprocessing_obj.transform(
                input_feature_test_df
            )

            train_arr = np.c_[
                input_feature_train_arr,
                target_feature_train_df.values
            ]

            test_arr = np.c_[
                input_feature_test_arr,
                target_feature_test_df.values
            ]

            logger.info("Saving Preprocessor Object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            logger.info("Data Transformation Completed")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)