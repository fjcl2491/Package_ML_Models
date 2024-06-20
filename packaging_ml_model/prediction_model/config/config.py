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
FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'LoanAmount',
            'Loan_Amount_Term', 'Credit_History','Property_Area']

# Numeric features
NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

# Categorical features
CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed','Credit_History','Property_Area']

# Features to encode
FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed','Credit_History','Property_Area']

FEATURE_TO_MODIFY = ['ApplicantIncome']
FEATURE_TO_ADD = ['CoApplicantIncome']