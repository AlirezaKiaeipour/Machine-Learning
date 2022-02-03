# Water Quality EDA & Model

  - EDA:
    - [x]  Analysis Dataset
    - [x]  Chart to visualize the dataset

  - Preprocessing:
  
    - [x]  Fix missing values using data mean
    - [x]  Scaling data using StandardScaler
    - [x]  Our data is not balanced and I have to balance it
    
    ![2022-02-03_20-30-39](https://user-images.githubusercontent.com/88143329/152391437-007cfa3d-ea32-4b5d-b2fa-e74a4d3acfe9.png)
    
    - [x] Balanced data using SMOTETomek

  - Model:

    - [x]  KNeighborsClassifier
    - [x]  SVC
    - [x]  RandomForestClassifier
    - [x]  GBoostingClassifier
    - [x]  CatBoostClassifier

  - Accuracy:

    Algorithm | Accuracy | Precision | Precision | F1-score |
    ------------- | ------------- | ------------- | ------------- | ------------- |
    KNeighbors | **80.39 %** | **76.43 %** | **89.43 %**  | **82.42 %** | 
    SVM | **68.21 %** | **70.67 %** | **65.20 %**  | **67.82 %** |
    RandomForest | **76.02 %** | **77.74 %** | **74.74 %**  | **76.21 %** |
    Gboost | **75.76 %** | **78.08 %** | **73.45 %**  | **75.69 %** |
    Catboost | **75.49 %** | **77.35 %** | **73.96 %**  | **75.62 %** |
    
