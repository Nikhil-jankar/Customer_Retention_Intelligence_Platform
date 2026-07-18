import sys
from dataclasses import dataclass

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from src.config import ARTIFACT_DIR
from src.exception import CustomException
from src.logger import logger
from src.utils import save_object


@dataclass
class ModelEvaluatorConfig:
    trained_model_file_path = ARTIFACT_DIR / "model.pkl"


class ModelEvaluator:

    def __init__(self):
        self.config = ModelEvaluatorConfig()

    def evaluate_models(
        self,
        trained_models,
        test_array
    ):

        try:

            logger.info("Starting Model Evaluation")

            X_test = test_array[:, :-1]
            y_test = test_array[:, -1]

            model_report = {}

            best_model = None
            best_model_name = None
            best_f1_score = -1

            for model_name, model in trained_models.items():

                logger.info(f"Evaluating {model_name}")

                y_pred = model.predict(X_test)

                accuracy = accuracy_score(y_test, y_pred)
                precision = precision_score(
                    y_test,
                    y_pred,
                    average="binary",
                    pos_label="Yes"
                )
                recall = recall_score(
                    y_test,
                    y_pred,
                    average="binary",
                    pos_label="Yes"
                )
                f1 = f1_score(
                    y_test,
                    y_pred,
                    average="binary",
                    pos_label="Yes"
                )

                try:
                    y_prob = model.predict_proba(X_test)[:, 1]

                    roc_auc = roc_auc_score(
                        (y_test == "Yes").astype(int),
                        y_prob
                    )

                except Exception:
                    roc_auc = None

                model_report[model_name] = {
                    "Accuracy": accuracy,
                    "Precision": precision,
                    "Recall": recall,
                    "F1 Score": f1,
                    "ROC AUC": roc_auc
                }

                if f1 > best_f1_score:
                    best_f1_score = f1
                    best_model = model
                    best_model_name = model_name

            logger.info(f"Best Model : {best_model_name}")

            save_object(
                self.config.trained_model_file_path,
                best_model
            )

            logger.info("Best Model Saved Successfully")

            print("\n" + "=" * 70)
            print("MODEL COMPARISON")
            print("=" * 70)

            for model_name, metrics in model_report.items():

                print(f"\n{model_name}")

                for metric_name, value in metrics.items():

                    if value is None:
                        print(f"{metric_name:<15}: N/A")
                    else:
                        print(f"{metric_name:<15}: {value:.4f}")

            print("\n" + "=" * 70)
            print(f"Best Model : {best_model_name}")
            print("=" * 70)

            return best_model_name, model_report

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)