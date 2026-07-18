import sys
from dataclasses import dataclass

from sklearn.ensemble import (
    GradientBoostingClassifier,
    RandomForestClassifier
)
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from src.exception import CustomException
from src.logger import logger


@dataclass
class ModelTrainerConfig:
    """
    Future configuration placeholder.
    """
    pass


class ModelTrainer:

    def __init__(self):
        self.config = ModelTrainerConfig()

    def initiate_model_training(self, train_array):

        try:

            logger.info("Starting Model Training")

            X_train = train_array[:, :-1]

            y_train = train_array[:, -1]

            models = {

                "Logistic Regression": LogisticRegression(
                    max_iter=1000,
                    random_state=42
                ),

                "Decision Tree": DecisionTreeClassifier(
                    random_state=42
                ),

                "Random Forest": RandomForestClassifier(
                    random_state=42
                ),

                "Gradient Boosting": GradientBoostingClassifier(
                    random_state=42
                )

            }

            trained_models = {}

            for name, model in models.items():

                logger.info(f"Training {name}")

                model.fit(X_train, y_train)

                trained_models[name] = model

            logger.info("All Models Trained Successfully")

            return trained_models

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)