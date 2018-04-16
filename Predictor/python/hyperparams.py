try:
    import os
    import sys
    import numpy as np
    import pandas as pd
    from sklearn import metrics
    import simplejson as json
    import trained_model as tm
    returnedData = []	
    count = 1

    while True:
        #print("{0:.2f}".format(count/100))
        if count == 100:
            break;
        try:
            predict_test = getNuSVCModelAccuracy(count/100).predict(x_train)
        except Exception as e:
            #print("{0:.2f}".format(count/100) + " is infeasable")
            count = count + 1
            continue
        conf_array = metrics.confusion_matrix(y_train, predict_test)

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
                "precision" : round(metrics.precision_score(y_train, predict_test),2)*100,
                "sensitvity" : round(metrics.recall_score(y_train, predict_test),2)*100,
                "specificity" : round(true_neg/(true_neg + false_pos),2)*100,
                "accuracy" : round(metrics.accuracy_score(y_train, predict_test),2)*100,
                "nu":count/100
                }
        returnedData.append(data)
        count = count + 1
    print(json.dumps(returnedData), end="")