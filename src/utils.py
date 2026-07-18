import os
import sys
import joblib

from src.exception import CustomException


def save_object(file_path, obj):
    """
    Save any Python object (model, pipeline, encoder, etc.)
    """

    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        joblib.dump(obj, file_path)

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    """
    Load saved Python object
    """

    try:
        return joblib.load(file_path)

    except Exception as e:
        raise CustomException(e, sys)
    
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


def evaluate_models(X_train, y_train, X_test, y_test, models):
    """
    Train and evaluate multiple models.
    Returns a dictionary of model scores.
    """

    report = {}

    for model_name, model in models.items():

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        precision = precision_score(
            y_test,
            predictions,
            pos_label="Yes"
        )

        recall = recall_score(
            y_test,
            predictions,
            pos_label="Yes"
        )

        f1 = f1_score(
            y_test,
            predictions,
            pos_label="Yes"
        )

        report[model_name] = {
            "model": model,
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1
        }

    return report