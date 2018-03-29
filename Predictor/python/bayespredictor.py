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
    from trained_model import nb_model
    from trained_model import pp
    
    x_single = [Decimal(n) for n in sys.argv[2].split(",")]
    x_single = pp.StandardScaler().fit_transform([x_single])

    # Calculate record probability as percent
    probabilityOfDiabetes = nb_model.decision_function(x_single)[0]
    print(round(probabilityOfDiabetes,2) * 100, end="")

except Exception as e:
    print ("Unexpected error:", format(e) )