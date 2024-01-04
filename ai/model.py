#importing basic packages
import pandas as pd

#Loading the data
df = pd.read_csv('ai/dataset/smol-data.csv')

#Dropping the Domain column
df = df.drop(['url'], axis = 1)
X = df.drop(['label'], axis = 1)
Y = df['label']

df = df.sample(frac=1).reset_index(drop=True)

# Splitting the dataset into train and test sets: 80-20 split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.4, random_state = 42)

 #XGBoost Classification model
from xgboost import XGBClassifier

#importing packages
from sklearn.metrics import accuracy_score

# instantiate the model
xgb = XGBClassifier(
        learning_rate=0.01,
        max_depth=50,
        n_estimators=300,
        n_jobs=-1,
)

#fit the model
xgb.fit(X_train, y_train)

#predicting the target value from the model for the samples
y_test_xgb = xgb.predict(X_test)
y_train_xgb = xgb.predict(X_train)

#computing the accuracy of the model performance
acc_train_xgb = accuracy_score(y_train,y_train_xgb)
acc_test_xgb = accuracy_score(y_test,y_test_xgb)

print("XGBoost: Accuracy on training Data: {:.3f}".format(acc_train_xgb))
print("XGBoost : Accuracy on test Data: {:.3f}".format(acc_test_xgb))

# save XGBoost model to file
import pickle
pickle.dump(xgb, open("ai/model.pickle", "wb"))
