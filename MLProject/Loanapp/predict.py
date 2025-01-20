import numpy as np
import joblib
import pandas as pd

import sys
import os
config_root = os.path.dirname(os.path.abspath(__file__))
#print(config_root)
sys.path.append(config_root)


from config import config
from processing.data_handling import load_data,load_pipeline

_model = load_pipeline(config.MODEL_NAME)

'''
def generate_predictions():
    test_data = load_data(config.TEST_FILE)
    pred = _model.predict(test_data[config.FEATURES])
    result = {"Predictions" : pred}
    print(result)
    return result
'''
def generate_predictions(data_input):
    try:
        data = pd.DataFrame(data_input , columns = config.FEATURES)
    except Exception as e:
        print(e)

    if data.empty:
        print("The input dataset is empty. Returning empty prediction.")
        return {"Predictions" : []}
    
    pred = _model.predict(data)
    status = lambda x : 'Y' if x == 1 else 'N'
    result = {"Predictions" : status(pred)}
    return result


if __name__ == '__main__':
    generate_predictions()
