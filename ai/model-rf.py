#importing basic packages
import pandas as pd

#Loading the data
df = pd.read_csv('ai/dataset/url-combined-dataset.csv')

#Dropping the Domain column
df = df.drop(['url'], axis = 1)
X = df.drop(['label'], axis = 1)
Y = df['label']

# Splitting the dataset into train and test sets: 80-20 split
from sklearn.model_selection import GridSearchCV, train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

 #XGBoost Classification model
from xgboost import XGBClassifier

#importing packages
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

modelRF = RandomForestClassifier(
    n_estimators = 50,
    criterion = 'gini',
    max_depth = None,
    min_samples_split = 2,
    min_samples_leaf = 1,
    min_weight_fraction_leaf = 0.0,
    max_features = 'log2',
    max_leaf_nodes = None,
    min_impurity_decrease = 0.0,
    bootstrap = True,
    oob_score = False,
    n_jobs = None,
    random_state = 1050,
    verbose = 0,
    warm_start = False,
    ccp_alpha = 0.0,
    max_samples = None
)

hyperparam = { 'n_estimators': [50, 75, 100, 125, 150] }

clf = GridSearchCV(
        estimator=modelRF,
        param_grid=hyperparam,
        cv=2,
        verbose=1,
        n_jobs=-1
)

clf.fit(X=X_train, y=y_train)

for i in range(len(clf.cv_results_['params'])):
    print("Params:", clf.cv_results_['params'][i])
    print("Mean accuracy:", clf.cv_results_['mean_test_score'][i])

RFModel = clf.best_estimator_
predictions = RFModel.predict(X_test)

print(classification_report(y_test, predictions))

import pickle

pickle.dump(RFModel, open("ai/model_rf.pickle", "wb"))
