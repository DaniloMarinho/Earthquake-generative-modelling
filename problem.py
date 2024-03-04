import os
import pandas as pd
import rampwf as rw
from sklearn.model_selection import ShuffleSplit

problem_title = 'Earthquake generative modelling'

# Setting up regression workflow
Predictions = rw.prediction_types.make_regression()

workflow = rw.workflows.Regressor()

# RMSE SCORE
score_types = [
    rw.score_types.RMSE()
]

# Cross-validation scheme
def get_cv(X, y):
    cv = ShuffleSplit(n_splits=3, test_size=0.2, random_state=42)
    return cv.split(X)

# I/O methods
_target_column_name = "Time5"
_ignore_column_names = []

def _read_data(path, f_name):
    data = pd.read_csv(os.path.join(path, 'data', f_name))
    y_array = data[_target_column_name].values
    X_df = data.drop([_target_column_name] + _ignore_column_names, axis=1).values
    return X_df, y_array

def get_train_data(path='.'):
    f_name = 'train.csv'
    return _read_data(path, f_name)

def get_test_data(path='.'):
    f_name = 'test.csv'
    return _read_data(path, f_name)