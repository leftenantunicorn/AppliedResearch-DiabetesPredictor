#########################################################
## Get data about the trained model

try:
    import sys
    import numpy as np
    import pandas as pd
    from decimal import Decimal
    from sklearn.preprocessing import Imputer
    from sklearn.naive_bayes import GaussianNB
    from sklearn.cross_validation import train_test_split
    from sklearn import metrics
    import simplejson as json
    import os

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
    fill_0 = Imputer(missing_values=0, strategy="mean", axis=0)
    x_train = fill_0.fit_transform(x_train)
    x_test = fill_0.fit_transform(x_test)

    # Train model
    nb_model = GaussianNB()
    nb_model.fit(x_train, y_train.ravel())

    # Report on accuracies
    nb_predict_test = nb_model.predict(x_test)
    conf_array = metrics.confusion_matrix(y_test, nb_predict_test)
    
    true_pos = conf_array[1][1]
    true_neg = conf_array[0][0]
    false_pos = conf_array[0][1]
    false_neg  = conf_array[1][0]

    data = {"conf" : {
                "true_pos" : round(np.int64(true_pos).item(),2),
                "true_neg" : round(np.int64(true_neg).item(),2),
                "false_pos" : round(np.int64(false_pos).item(),2),
                "false_neg"  : round(np.int64(false_neg).item(),2),
                }, 
            "precision" : round(metrics.precision_score(y_test, nb_predict_test),2)*100,
            "sensitvity" : round(metrics.recall_score(y_test, nb_predict_test),2)*100,
            "specificity" : round(true_neg/(true_neg + false_pos),2)*100,
            "accuracy" : round(metrics.accuracy_score(y_test, nb_predict_test),2)*100,
           }

    print(json.dumps(data), end="")

except Exception as e:
    print ("Unexpected error:", format(e) )