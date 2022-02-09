# Boston House Price Model

  **Dataset Link:** [Boston House Prices](https://www.kaggle.com/fedesoriano/the-boston-houseprice-data)

  - Preprocessing:

    - [x]  Scaling data using StandardScaler
 
  - Model:

    - [x]  LinearRegression
    - [x]  SVR
    - [x]  RandomForestRegressor
    - [x]  AdaBoostRegressor
    - [x]  GBoostingRegressor
    - [x]  XGboostRegressor
    - [x]  CatBoostRegressor

  - Score:

    Algorithm | MAE | MSE | R2-Score |
    ------------- | ------------- | ------------- | ------------- |
    LinearRegression | **2.979** | **16.538367** | **78.49 %**  |
    SVR | **2.536** | **15.342723** | **80.04 %**  |
    RandomForest | **2.266** | **12.604454** | **83.60 %**  |
    AdaBoost | **2.037** | **10.375075** | **86.50 %**  |
    GBoost | **2.399** | **10.375075** | **83.60 %**  |
    XGBoost | **2.364** | **12.508929** | **83.73 %**  |
    CatBoost | **1.941** | **12.508929** | **90.61 %**  |
    
