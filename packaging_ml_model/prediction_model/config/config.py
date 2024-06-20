import pathlib
import os
import prediction_model

# Return me the path where exactly my init file is present
PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

TRAIN_FILE = "train.csv"
TEST_FILE = "test.csv"

MODEL_NAME = "classification.pkl"
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, "trained_models")

# The variable you want to predict based on the relation between the features
TARGET = "Loan_Status"

# Final features used in the model to predict the target
FEATURES = []

# Numeric features
NUM_FEATURES = []

# Categorical features
CAT_FEATURES = []

# Features to encode
FEATURES_TO_ENCODE = []