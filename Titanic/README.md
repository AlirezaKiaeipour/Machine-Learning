# Titanic Dataset EDA

### Data Preprocessing:

  - Drop Useless columns
  - One Hot Encoder
  - Fix missing values useing KNNImputer
  - Scaling data using StandardScaler

  ![2022-02-01_21-30-31](https://user-images.githubusercontent.com/88143329/152024685-1297024c-e04a-4db0-a2c8-ce5096a9eb50.png)
  
  - balance data using SMOTETomek

### Machine Learning Algorithm:
- Modeling:

  - KNeighborsClassifier
  - SVM
  - RandomForestClassifier
  - AdaBoostClassifier
  - GBoostingClassifier
  - XGBoostClassifier
  - CatBoostClassifier

### Accuracy:

  Algorithm | Accuracy | Precision | Recall | F1-score |
----- | ----- | ----- | ----- | ----- |
KNeighbors | **86 %** | **87 %** | **87 %**  | **87 %**  | 
SVM | **82 %** | **87 %** | **79 %** | **83 %** |
RandomForest | **93 %** | **95 %** | **92 %** | **93 %** |
Adaboost | **84 %** | **86 %** | **84 %** | **85 %** |
Gboost | **86 %** | **89 %** | **85 %** | **87 %** | 
XGboost | **86 %** | **89 %** | **84 %** | **87 %** |
Catboost | **92 %** | **93 %** | **92 %** | **92 %** |
