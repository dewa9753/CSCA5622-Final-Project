from sklearn.model_selection import train_test_split
import sys
import os
import pandas as pd
import numpy as np
import joblib
from lib.settings import MODEL_ROOT, DATA_ROOT, MODEL_NAME, RANDOM_STATE, TEST_SIZE, CV_FOLD, N_JOBS
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import GridSearchCV

def cv_hyperparameters(X, y):
    # kind of randomly chose the grid to search over
    grid = {
        'n_estimators': list(np.arange(50, 500, 50)),
        'max_depth': [None] + list(np.arange(1, 50, 5)), # unlimited depth may be the best, who knows
        'min_samples_split': list(np.arange(5, 20, 2)),
    }

    rf = RandomForestClassifier(random_state=RANDOM_STATE)
    print("Starting grid search...")
    grid_search = GridSearchCV(estimator=rf, param_grid=grid, cv=CV_FOLD, n_jobs=N_JOBS, scoring='accuracy')
    grid_search.fit(X, y)
    print("Grid search complete.")

    return grid_search.best_params_

def train_model(X, y, params=dict()):
    if not params:
        # choose default parameters
        params = {
            'n_estimators': 100,
            'max_depth': None,
            'min_samples_split': 2,
        }

    model = RandomForestClassifier(random_state=RANDOM_STATE, **params) # ** --> unpack dictionary into keyword arguments
    model.fit(X, y)

    return model

def test_model(model, X_test, y_test):
    yhat = model.predict(X_test)
    return accuracy_score(y_test, yhat)

def load_model(model_name):
    return joblib.load(f'{MODEL_ROOT}/{model_name}.joblib')

def save_model(model):
    if not os.path.exists(MODEL_ROOT):
        os.makedirs(MODEL_ROOT)
    joblib.dump(model, f'{MODEL_ROOT}/{MODEL_NAME}.joblib')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--force-train':
            import shutil
            if os.path.exists(MODEL_ROOT):
                print("Forcing re-training of models...")
                shutil.rmtree(MODEL_ROOT)
                print(f"Removed existing model directory '{MODEL_ROOT}'.")
    
    if not os.path.exists(f'{MODEL_ROOT}/{MODEL_NAME}.joblib'):
        df = pd.read_csv(f'{DATA_ROOT}/final_data.csv')
        X = df.drop(columns=['finalPosition'])
        y = df['finalPosition']

        # split data, cross-validation, and train model
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)

        print("Tuning hyperparameters...")
        best_params = cv_hyperparameters(X_train, y_train)

        print(f"Found the best parameters: {best_params}")

        print("Training model...")
        model = train_model(X_train, y_train, best_params)

        # test model
        acc = test_model(model, X_test, y_test)
        print(f'Model test accuracy: {acc}')
        f1 = f1_score(y_test, model.predict(X_test), average='weighted')
        print(f'Model test F1 score: {f1}')


        # ask if the user wants to save the model
        print("Would you like to save this model? (y/n): ")
        user_input = input().strip().lower()
        if user_input == 'y':
            save_model(model)
            print(f'Model saved in {MODEL_ROOT}/{MODEL_NAME}.joblib')
    else:
        print('Loading existing model...')
        model = load_model(MODEL_NAME)

        df = pd.read_csv(f'{DATA_ROOT}/final_data.csv')
        X = df.drop(columns=['finalPosition'])
        y = df['finalPosition']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)

        score = test_model(model, X_test, y_test)
        print(f'Model test accuracy: {score}')