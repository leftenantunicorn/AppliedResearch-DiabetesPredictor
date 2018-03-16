

# coding: utf-8

# In[4]:

import numpy as np
import pandas as pd

df = pd.read_csv("pima-data.csv")

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
print("hello")

# In[11]:


from sklearn.cross_validation import train_test_split

feature_col_names = ['num_preg', 'glucose_conc', 'diastolic_bp', 'thickness', 'insulin', 'bmi', 'diab_pred', 'age']
predicted_class_names = ['diabetes']

X = df[feature_col_names].values
y = df[predicted_class_names].values
split_test_size = 0.20

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_test_size, random_state=42) 


# In[13]:


from sklearn.preprocessing import Imputer

fill_0 = Imputer(missing_values=0, strategy="mean", axis=0)

X_train = fill_0.fit_transform(X_train)
X_test = fill_0.fit_transform(X_test)


# In[14]:


from sklearn.naive_bayes import GaussianNB

# create Gaussian Naive Bayes model object and train it with the data
nb_model = GaussianNB()

nb_model.fit(X_train, y_train.ravel())


nb_predict_train = nb_model.predict(X_train)


# In[25]:


def predictSingleRecord(record):
    X_single = np.array(record).reshape(1,8)
    return nb_model.predict(X_single)

