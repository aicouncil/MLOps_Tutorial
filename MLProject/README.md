# Loanapp

This document provides an overview of the directory structure and key components of the `Loanapp` project.

## Directory Structure

```
MLProject
├──Loanapp
    ├── config/
    │   ├── __init__.py
    │   └── config.py
    ├── datasets/
    │   ├── loanTrain.csv
    │   └── test_loan.csv
    ├── processing/
    │   ├── __init__.py
    │   ├── data_handling.py
    │   └── preprocessing.py
    ├── trained_models/
    │   └── classification.pkl
    ├── VERSION
    ├── __init__.py
    ├── pipeline.py
    ├── predict.py
    ├── training_pipeline.py
    ├── MANIFEST.in
├──tests
    ├──test_predictions.py
├── README.md
├── requirements.txt
└── setup.py
```

## Folder Descriptions

### config/
Contains configuration files and settings for the application.
- `__init__.py`: Marks the directory as a Python package.
- `config.py`: Contains configuration variables such as file paths and model settings.

### datasets/
Stores training and testing datasets.
- `loanTrain.csv`: Training dataset.
- `test_loan.csv`: Testing dataset.

### processing/
Holds scripts for data preprocessing and handling.
- `__init__.py`: Marks the directory as a Python package.
- `data_handling.py`: Functions to load and preprocess datasets.
- `preprocessing.py`: Additional data preprocessing utilities.

### trained_models/
Contains the trained machine learning model(s).
- `classification.pkl`: Serialized classification model.

## File Descriptions

- **VERSION**: Contains the current version of the application.
- **__init__.py**: Initializes the main Python package.
- **pipeline.py**: Defines the data processing and model pipeline.
- **predict.py**: Contains the logic to generate predictions using the trained model.
- **training_pipeline.py**: Script to train the machine learning model.
- **MANIFEST.in**: Specifies additional files to include in the Python package.
- **README.md**: Documentation for the application.
- **requirements.txt**: Lists the dependencies required for the project.
- **setup.py**: Configuration script for packaging and installing the application.

## Usage

### Setup
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Train the model:
   ```bash
   python training_pipeline.py
   ```

3. Generate predictions:
   ```bash
   python predict.py
   ```

### Testing
Run the test suite using `pytest`:
```bash
pytest
```

## Contribution
Feel free to raise issues or submit pull requests to improve the project.
