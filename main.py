from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluator


if __name__ == "__main__":

    ingestion = DataIngestion()

    train_path, test_path = ingestion.initiate_data_ingestion()

    validator = DataValidation()

    validator.validate_dataset()

    transformer = DataTransformation()

    train_arr, test_arr, _ = transformer.initiate_data_transformation(
        train_path,
        test_path
    )

    trainer = ModelTrainer()

    trained_models = trainer.initiate_model_training(
        train_arr
    )

    evaluator = ModelEvaluator()

    best_model, report = evaluator.evaluate_models(
        trained_models,
        test_arr
    )

    print("\nTraining Pipeline Completed Successfully")