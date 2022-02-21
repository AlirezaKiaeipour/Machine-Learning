# Titanic EDA & Model

  **Dataset Link:** [Titanic](https://www.kaggle.com/c/titanic/data?select=train.csv)

  - EDA:
    - [x]  Analysis Dataset
    - [x]  Chart to visualize the Titanic Dataset

  - Preprocessing:
  
    - [x]  Fix missing values using KNNImputer
    - [x]  Convert Categorical to Numerical using One Hot Encoder
    - [x]  Scaling data using StandardScaler
    - [x]  Our data is not balanced and I have to balance it
    
    ![2022-02-02_23-56-41](https://user-images.githubusercontent.com/88143329/152232085-5f061c42-2ba2-4124-b8a8-6c2313b5f834.png)
    
    - [x] Balanced data using SMOTETomek

  - Model:

    - [x]  KNeighborsClassifier
    - [x]  SVC
    - [x]  RandomForestClassifier
    - [x]  AdaBoostClassifier
    - [x]  GBoostingClassifier
    - [x]  XGBoostClassifier
    - [x]  CatBoostClassifier
    - [x]  Perceptron
    - [x]  Multi Layer Perceptron

  - Accuracy:

    Algorithm | Accuracy | Precision | Recall | F1-score |
    ------------- | ------------- | ------------- | ------------- | ------------- |
    KNeighbors | **86.13 %** | **87.61 %** | **87.61 %**  | **87.61 %** | 
    SVM | **82.17 %** | **87.37 %** | **79.64 %**  | **83.33 %** |
    RandomForest | **93.06 %** | **95.41 %** | **92.03 %**  | **93.69 %** |
    Adaboost | **84.15 %** | **86.48 %** | **84.95 %**  | **85.71 %** |
    Gboost | **86.63 %** | **89.81 %** | **85.84 %**  | **87.78 %** |
    XGboost | **86.13 %** | **89.71 %** | **84.95 %**  | **87.27 %** |
    Catboost | **92.07 %** | **93.69 %** | **92.03 %**  | **92.85 %** |
    Perceptron | **78.21 %** | **84.15 %** | **75.22 %**  | **79.43 %** |
    MLP | **93.06 %** | **89.74 %** | **92.92 %**  | **91.30 %** |
    
