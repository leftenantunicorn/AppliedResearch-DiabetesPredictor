﻿#########################################################
## Make model

try:
    import sys
    import numpy as np
    import pandas as pd
    from decimal import Decimal
    import sklearn.preprocessing as pp
    from sklearn.naive_bayes import GaussianNB
    from sklearn.cross_validation import train_test_split
    from sklearn import svm
    import simplejson as json
    import os
    from sklearn.preprocessing import binarize
    from sklearn import metrics
    import sklearn
    from sklearn import linear_model

    # Get training data
    df = pd.read_csv(sys.argv[1])

    # Prepare feature and result sets
    feature_col_names = ['num_preg', 'glucose_conc', 'diastolic_bp', 'thickness', 'insulin', 'bmi', 'diab_pred', 'age']
    predicted_class_names = ['diabetes']

    x = df[feature_col_names].values
    y = df[predicted_class_names].values

    # Split data into train and test sets
    split_test_size = 0.20
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=split_test_size, random_state=73) 

    # Manipulate bad data
    fill_0 = pp.Imputer(missing_values=0, strategy="mean", axis=0)
    x_train = fill_0.fit_transform(x_train)
    scaler = pp.StandardScaler()

    ## train with x, y to use full data set
    # Train model - Naive Bayes
    def getBayesModel():
        nb_model = GaussianNB(priors=[0.45,0.55])
        nb_model.fit(x_train, y_train.ravel())
        return nb_model

    # Train model - SVM
    def getSVCModel():
    # Set the parameters by cross-validation
        global x_train
        global x_test
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.fit_transform(x_test)
        svc_model = svm.SVC(gamma=0.001,C=10000,kernel="rbf")
        svc_model.fit(x_train, y_train.ravel()) 
        return svc_model

    def getNuSVCModel():
    # Set the parameters by cross-validation
        global x_train
        global x_test
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.fit_transform(x_test)
        nuSvc_model = svm.NuSVC(class_weight=None, coef0=0.0, gamma=0.1, kernel='rbf', 
          nu=0.47, probability=False, random_state=0)
        nuSvc_model.fit(x_train, y_train.ravel()) 
        return nuSvc_model

    def getLogisticRegressionModel():
        lr_model = linear_model.LogisticRegression()
        lr_model.fit(x_train, y_train.ravel())
        return lr_model


    model = getNuSVCModel()

except Exception as e:
    print ("Unexpected error:", format(e) )