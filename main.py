
import tensorflow as tf 
from tensorflow.keras.models import Sequential 
import pickle 
import numpy as np 


def CreateModel() -> Sequential:
  model = tf.keras.models.Sequential()
  model.add(tf.keras.layers.Dense(units = 1500, activation="relu"))
  model.add(tf.keras.layers.Dense(units = 1024, activation="relu"))
  model.add(tf.keras.layers.Dense(units = 512, activation="relu"))
  model.add(tf.keras.layers.Dense(units = 128, activation="relu"))
  model.add(tf.keras.layers.Dense(units = 32, activation="relu"))
  model.add(tf.keras.layers.Dense(units = 6, activation="sigmoid"))
  model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
  return model


Model = CreateModel()
Model.load_weights("weights/DenseModel")

CV = None
Encoder = None 

with open("Vectorizer.pkl", "rb") as f:
    CV = pickle.loads(f.read())

with open("encoder.pkl", "rb") as f:
    Encoder = pickle.loads(f.read())


def MakePred(ANN):
    print(CV.__class__)
    UserInput = input("> ")
    string = np.array([UserInput]) 
    print(ANN)
    string = CV.transform(string).toarray()
    print(string)
    pred = ANN.predict(np.array([string]))
    print(pred)

MakePred(Model)






