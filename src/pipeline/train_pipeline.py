from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluator

from src.logger import logger


class TrainPipeline:

    def __init__(self):
        pass

    def run_pipeline(self):

        logger.info("=" * 80)
        logger.info("TRAINING PIPELINE STARTED")
        logger.info("=" * 80)

        # -----------------------------
        # Step 1 : Data Ingestion
        # -----------------------------
        ingestion = DataIngestion()

        train_path, test_path = ingestion.initiate_data_ingestion()

        logger.info("Data Ingestion Completed")

        # -----------------------------
        # Step 2 : Data Validation
        # -----------------------------
        validator = DataValidation()

        validator.validate_dataset()

        logger.info("Data Validation Completed")

        # -----------------------------
        # Step 3 : Data Transformation
        # -----------------------------
        transformer = DataTransformation()

        train_arr, test_arr, preprocessor_path = (
            transformer.initiate_data_transformation(
                train_path,
                test_path
            )
        )

        logger.info("Data Transformation Completed")

        # -----------------------------
        # Step 4 : Model Training
        # -----------------------------
        trainer = ModelTrainer()

        trained_models = trainer.initiate_model_training(
            train_arr
        )

        logger.info("Model Training Completed")

        # -----------------------------
        # Step 5 : Model Evaluation
        # -----------------------------
        evaluator = ModelEvaluator()

        best_model, report = evaluator.evaluate_models(
            trained_models,
            test_arr
        )

        logger.info("Model Evaluation Completed")

        logger.info(f"Best Model : {best_model}")

        logger.info("=" * 80)
        logger.info("TRAINING PIPELINE COMPLETED")
        logger.info("=" * 80)

        return {
            "best_model": best_model,
            "report": report,
            "preprocessor_path": preprocessor_path
        }


if __name__ == "__main__":

    pipeline = TrainPipeline()

    result = pipeline.run_pipeline()

    print("\n")
    print("=" * 80)
    print("PIPELINE EXECUTED SUCCESSFULLY")
    print("=" * 80)

    print(f"Best Model : {result['best_model']}")