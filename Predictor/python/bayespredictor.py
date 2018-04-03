﻿#########################################################
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
    
    if(isinstance(tm.model, sklearn.svm.classes.SVC) or isinstance(tm.model, sklearn.svm.classes.NuSVC) ) :
        x_single = tm.scaler.fit_transform(x_single)
        

    # Calculate record probability as percent
    probabilityOfDiabetes = tm.model.predict_proba(x_single)[0][1]

    print(round(probabilityOfDiabetes,2) * 100, end="")

except Exception as e:
    print ("Unexpected error:", format(e) )