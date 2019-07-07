import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split #machine learning algorithm library

# importing train data
data1 = pd.read_csv("C:/Users/srinidhi/titanic/train.csv")

# Converting string data into numbers like 0,1,2
data1 = data1.replace(["male", "female"], [0,1])
data1 = data1.replace(["S", "C", "Q"], [0,1,2])
data1= data1.fillna(0) # to replace non numeric values by 0
y = data1[["Survived"]] 
X = data1[["PassengerId","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]

# convert to numpy array for NN
X = X.astype(np.float32).values
y = y.astype(np.float32).values

# import test data
data2 = pd.read_csv("C:/Users/srinidhi/titanic/test.csv")
data2 = data2.replace(["male", "female"], [0,1])
data2 = data2.replace(["S", "C", "Q"], [0,1,2])
data2= data2.fillna(0)
X_Test = data2[["PassengerId","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]
X_Test = X_Test.astype(np.float32).values
# Keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, BatchNormalization, Activation
from keras.wrappers.scikit_learn import KerasRegressor

seed = 42
np.random.seed(seed)
# data split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2)
# Model 
model = Sequential()
#input layer
model.add(Dense(8, input_shape=(8,)))
model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(Dropout(0.4))

# hidden layers
model.add(Dense(8))
model.add(BatchNormalization())
model.add(Activation("sigmoid"))
model.add(Dropout(0.4))
    
model.add(Dense(4))
model.add(BatchNormalization())
model.add(Activation("sigmoid"))
model.add(Dropout(0.4))
model.add(Dense(2, activation="sigmoid"))
    
# output layer
model.add(Dense(1, activation='linear'))
# model compile for binary classification
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# learning
model.fit(X, y, nb_epoch=500, batch_size=30)

# float to [0,1]
predictions = np.round(model.predict(X_Test))
predictions = pd.DataFrame(predictions)
# result
result = pd.concat([data1[["PassengerId"]], predictions], axis = 1)
predictions.to_csv("result.csv", index=False)