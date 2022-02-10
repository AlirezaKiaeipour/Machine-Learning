# Amsterdam House Price EDA & Model

  **Dataset Link:** [Amsterdam House Price](https://www.kaggle.com/thomasnibb/amsterdam-house-price-prediction)

  - EDA:
    - [x]  Analysis Dataset
    - [x]  Chart to visualize the Amsterdam House Price Dataset

  - Preprocessing:
  
    - [x]  Fix missing values using Remove that
    - [x]  Convert Categorical to Numerical using LabelEncoder
    - [x]  Scaling data using StandardScaler
 
  - Model:

    - [x]  LinearRegression
    - [x]  RandomForestRegressor
    - [x]  AdaBoostRegressor
    - [x]  CatBoostRegressor

  - Score:

    Algorithm | MAE | MSE | R2-Score |
    ------------- | ------------- | ------------- | ------------- |
    LinearRegression | **157402.64** | **4.772338e+10** | **77.95 %**  |
    RandomForest | **90246.11** | **3.260174e+10** | **84.94 %**  |
    AdaBoost | **91032.55** | **3.480491e+10	** | **83.92 %**  |
    CatBoost | **93689.10** | **4.781621e+10** | **77.91 %**  |
    

