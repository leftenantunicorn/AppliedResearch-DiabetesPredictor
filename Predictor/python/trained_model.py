﻿#########################################################
## Make model

try:
    import os
    import sys
    import numpy as np
    import pandas as pd
    import sklearn.preprocessing as pp
    from sklearn.cross_validation import train_test_split
    from sklearn import svm, linear_model, naive_bayes
    import simplejson as json
    from sklearn.pipeline import make_union, make_pipeline
    from sklearn.base import BaseEstimator, TransformerMixin

    # Get training data
    df = pd.read_csv(sys.argv[1])

    # Prepare feature and result sets
    feature_col_names_fullset = ['num_preg', 'glucose_conc', 'diastolic_bp', 'thickness', 'insulin', 'bmi', 'diab_pred', 'age']
    feature_col_names = ['num_preg', 'glucose_conc', 'bmi', 'diab_pred', 'age']
    predicted_class_names = ['diabetes']

    y = df[predicted_class_names].values

    fill_0 = pp.Imputer(missing_values=0, strategy="mean", axis=0)
    fill_insulin = pp.Imputer(missing_values=0, strategy="median", axis=0)
    scaler = pp.StandardScaler()
    
    # Manipulate bad data

    # from https://medium.com/@literallywords/sklearn-identity-transformer-fcc18bac0e98
    class IdentityTransformer(BaseEstimator, TransformerMixin):
        def __init__(self):
            pass

        def fit(self, input_array, y=None):
            return self

        def transform(self, input_array, y=None):
            return input_array * 1

    def get_invalid0_cols(df):
        return df[[ 'glucose_conc', 'diastolic_bp', 'bmi', 'diab_pred' ]]

    def get_valid0_cols(df):
        return df[['num_preg']]

    def get_insulin_cols(df):
        return df[['insulin']]

    vec = make_union(*[
        make_pipeline(pp.FunctionTransformer(get_valid0_cols, validate=False), IdentityTransformer()),
        make_pipeline(pp.FunctionTransformer(get_invalid0_cols, validate=False), fill_0)
        #make_pipeline(pp.FunctionTransformer(get_insulin_cols, validate=False), fill_insulin),
    ])
    x = vec.fit_transform(df)

    # Split data into train and test sets
    split_test_size = 0.20
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=split_test_size, random_state=73) 
    
    #For manual tuning
    #split_val_size = 0.20
    #x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=split_val_size, random_state=73) 

    # Train model - Accuracy Method of NuSVC
    def getNuSVCModelAccuracy(nuValue):
        global x_train
        global x_test
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)
        nuSvc_model = svm.NuSVC(class_weight=None, coef0=0.0, gamma=0.1, kernel='rbf', 
          nu=nuValue, probability=True, random_state=0)
        nuSvc_model.fit(x_train, y_train.ravel()) 
        return nuSvc_model

    # Train model - Naive Bayes
    def getBayesModel():
        nb_model = naive_bayes.GaussianNB(priors=[0.45,0.55])
        nb_model.fit(x_train, y_train.ravel())
        return nb_model

    # Train model - SVC
    def getSVCModel():
        global x_train
        global x_test
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)
        svc_model = svm.SVC(C=1000)
        svc_model.fit(x_train, y_train.ravel()) 
        return svc_model

    # Train model - SVC Linear
    def getSVCLinearModel():
        global x_train
        global x_test
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)
        svc_model = svm.SVC(kernel="linear")
        svc_model.fit(x_train, y_train.ravel()) 
        return svc_model

    # Train model - NuSVC
    def getNuSVCModel():
        global x_train
        global x_test
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)
        nuSvc_model = svm.NuSVC(coef0=0.0, kernel='linear', 
          nu=0.58, gamma=0.01, probability=True, random_state=0)
        nuSvc_model.fit(x_train, y_train.ravel()) 
        return nuSvc_model

    # Train model - Logistic Regression
    def getLogisticRegressionModel():
        lr_model = linear_model.LogisticRegression()
        lr_model.fit(x_train, y_train.ravel())
        return lr_model


    model = getNuSVCModel()

except Exception as e:
    print ("Unexpected error:", format(e) )