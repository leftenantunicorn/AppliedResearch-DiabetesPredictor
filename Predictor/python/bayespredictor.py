#########################################################
## Make prediction for single record

try:
    import sys
    import numpy as np
    import pandas as pd
    from decimal import Decimal
    from sklearn.preprocessing import Imputer
    from sklearn.naive_bayes import GaussianNB
    from sklearn.cross_validation import train_test_split

    df = pd.read_csv(sys.argv[1])
    
    x_single = [Decimal(n) for n in sys.argv[2].split(",")];

    # Prepare feature and result sets
    feature_col_names = ['num_preg', 'glucose_conc', 'diastolic_bp', 'thickness', 'insulin', 'bmi', 'diab_pred', 'age']
    predicted_class_names = ['diabetes']

    x_train = df[feature_col_names].values
    y_train = df[predicted_class_names].values

    # Manipulate bad data
    fill_0 = Imputer(missing_values=0, strategy="mean", axis=0)
    x_train = fill_0.fit_transform(x_train)

    # Train model
    nb_model = GaussianNB()
    nb_model.fit(x_train, y_train.ravel())
    nb_predict_train = nb_model.predict(x_train)

    # Calculate record probability as percent
    probabilityOfDiabetes = nb_model.predict_proba([x_single])[0][1]
    print(round(probabilityOfDiabetes,2) * 100, end="")

except Exception as e:
    print ("Unexpected error:", format(e) )