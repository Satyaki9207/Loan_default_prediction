## Loan Default Prediction

### Project background
A bank is interested in predicting which customers are likely to default on loans in advance.It can adjust customer's credit worthiness criteria accordingly and avoid giving out bad loans. It has collected data like credit utilization,age,past delinquency,debt ratio,income etc related to the customer. 

### Dependencies
+ Python 3.7 or higher
+ numpy
+ pandas 
+ matplotlib
+ seaborn
+ imblearn
+ scikit learn
+ keras
+ Tensorflow 2.0 or higher
+ xgboost


### Files in the repository
+ Credit_Default_prediction -- The file containing the code to generate the model and visualizations
+ cs-training.csv -- file containing training data
+ cs-test.csv  -- file containing test data
+ Data Dictionary.xls -- file containing variable descriptions
+ Predictions.csv -- file containing predictions for cs-test.csv
+ credit_default.h5 -- pretrained model for making predictions

### How to use the model
+ load dependencies in a jupyter notebook  
</code> model=keras.models.load_model(credit_default.h5)  
       pred= model.predict(X_test) 
 pred=[1 if x>0.55 else 0 for x in pred] </code>



### Results
A person's age and past history of late payments are the best indicators of credit default
