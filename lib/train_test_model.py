from sklearn.model_selection import train_test_split
import sys
import os
import pandas as pd
from settings import MODELS_ROOT, DATA_ROOT, MODEL_NAME

def train_model(X, y):
    pass

def test_model(model, X_test, y_test):
    pass

def load_model(model_name):
    pass

def save_model(model, model_name):
    pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--force-train':
            print("Forcing re-training of models...")
            import shutil
            if os.path.exists(MODELS_ROOT):
                shutil.rmtree(MODELS_ROOT)
                print(f"Removed existing model directory '{MODELS_ROOT}'.")
    
    if not os.path.exists(MODELS_ROOT):
        df = pd.read_csv(f'{DATA_ROOT}/final_data.csv')
        X = df.drop(columns=['finalPosition'])
        y = df['finalPosition']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = train_model(X_train, y_train)

        # test model
        score = test_model(model, X_test, y_test)
        print(f'Model test score: {score}')

        # ask if the user wants to save the model
        print("Would you like to save this model? (y/n): ")
        user_input = input().strip().lower()
        if user_input == 'y':
            save_model(model, MODEL_NAME)
            print(f'Model saved in {MODELS_ROOT}/')
    else:
        print('Loading existing model...')
        model = load_model(MODEL_NAME)