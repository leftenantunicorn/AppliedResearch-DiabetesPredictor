#########################################################
## Make prediction for single record

try:
    import sys
    import numpy as np
    import pandas as pd
    from decimal import Decimal
    from sklearn.preprocessing import Imputer
    import sklearn
    from sklearn.cross_validation import train_test_split
    import trained_model as tm
    
    x_single = [[Decimal(n) for n in sys.argv[2].split(",")]]
    
    if(isinstance(tm.model, sklearn.svm.classes.SVC)) :
        x_single = tm.scaler.fit_transform(x_single)
        

    # Calculate record probability as percent
    probabilityOfDiabetes = tm.model.predict_proba(x_single)[0][1]

    # Set the parameters by cross-validation
    tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                         'C': [1, 10, 100, 1000]},
                        {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

    #clf = sklearn.model_selection.GridSearchCV(sklearn.svm.SVC(), tuned_parameters, cv=5,
                       scoring='accuracy')
    clf.fit(tm.x_train,tm.y_train)

    #print(round(probabilityOfDiabetes,2) * 100, end="")
    print(clf.best_params_)

except Exception as e:
    print ("Unexpected error:", format(e) )