from sklearn.ensemble import RandomForestClassifier
from pathlib import Path
import pandas as pd
import joblib 

MODEL_PATH = Path('resources/models/random_forest_model.joblib')

def main():
    model:RandomForestClassifier = joblib.load(MODEL_PATH)
    y_pred = "hello"
    features = ['up_total_bought', 'user_total_orders', 'user_avg_days_between', 'prod_total_purchases', 'prod_reorder_ratio']
    df = pd.DataFrame([[3, 4, 10, 4, 3], 
                       [0, 0, 0, 0, 0],
                       [10, 10, 10, 10, 10]],
                      columns=features)
    y_pred = model.predict(df)
    print(y_pred)

if __name__ == "__main__":
    main()