#########################################################
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

    x_train = pp.StandardScaler().fit_transform(x_train)
    x_test = pp.StandardScaler().fit_transform(x_test)

    ## train with x, y to use full data set
    # Train model - Naive Bayes
    nb_model_nb = GaussianNB(priors=[0.5, 0.5])
    nb_model_nb.fit(x_train, y_train.ravel()) 

    # Train model - SVM
    nb_model = svm.SVC(C=10.0, gamma= 0.01)
    nb_model.fit(x_train, y_train.ravel()) 

except Exception as e:
    print ("Unexpected error:", format(e) )