import numpy as np
import joblib
import pandas as pd

from config import config
from processing.data_handling import load_data,load_pipeline

_model = load_pipeline(config.MODEL_NAME)

def generate_predictions():
    test_data = load_data(config.TEST_FILE)
    pred = _model.predict(test_data[config.FEATURES])
    result = {"Predictions" : pred}
    print(result)
    return result

if __name__ == '__main__':
    generate_predictions()