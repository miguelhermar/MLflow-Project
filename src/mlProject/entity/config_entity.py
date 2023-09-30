from dataclasses import dataclass # define the variable instead of using "self" for classes
from pathlib import Path


@dataclass(frozen=True) # not a python class, but a data class
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float # inside the params.yaml
    l1_ratio: float  # inside the params.yaml
    target_column: str # gets it from schema.yaml

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict # comes from params.yaml
    metric_file_name: Path
    target_column: str
    mlflow_uri: str