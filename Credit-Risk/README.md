# Credit Risk EDA & Model

  **Dataset Link:** [Credit Risk](https://www.kaggle.com/praveengovi/credit-risk-classification-dataset)

  - EDA:
    - [x]  Analysis Dataset
    - [x]  Chart to visualize the Credit Risk Dataset

  - Preprocessing:
  
    - [x]  Fix missing values using SimpleImputer-Mean
    - [x]  Our data is not balanced and I have to balance it
    
    ![1](https://user-images.githubusercontent.com/88143329/153479633-7d63a7df-bde7-4adb-8f41-7e0b37933d76.png)
    
    - [x] Balanced data using SMOTEENN

  - Model:

    - [x]  KNeighborsClassifier
    - [x]  RandomForestClassifier
    - [x]  AdaBoostClassifier
    - [x]  GBoostingClassifier

  - Accuracy:

    Algorithm | Accuracy | Precision | Precision | F1-score |
    ------------- | ------------- | ------------- | ------------- | ------------- |
    KNeighbors | **94.24 %** | **94.73 %** | **94.73 %**  | **94.73 %** | 
    RandomForest | **95.68 %** | **97.29 %** | **94.73 %**  | **96.00 %** |
    AdaBoost | **94.96 %** | **96.00 %** | **94.73 %**  | **95.36 %** |
    GBoost | **95.68 %** | **97.29 %** | **94.73 %**  | **96.00 %** |
    
