#########################################################
## Get data about the trained model

try:
    import os
    import sys
    import numpy as np
    import pandas as pd
    from sklearn import metrics
    import simplejson as json
    import trained_model as tm

    # Report on accuracies
    predict_test = tm.model.predict(tm.x_test)
    conf_array = metrics.confusion_matrix(tm.y_test, predict_test)
    
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
            "precision" : round(metrics.precision_score(tm.y_test, predict_test),2)*100,
            "sensitvity" : round(metrics.recall_score(tm.y_test, predict_test),2)*100,
            "specificity" : round(true_neg/(true_neg + false_pos),2)*100,
            "accuracy" : round(metrics.accuracy_score(tm.y_test, predict_test),2)*100,
            "thing" : predict_test.tolist(),
            "thing" : tm.x_test.tolist()
           }

    print(json.dumps(data), end="")

except Exception as e:
    print ("Unexpected error:", format(e) )