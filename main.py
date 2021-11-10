
import tensorflow as tf 
from tensorflow.keras.models import Sequential 
import pickle 
import numpy as np 


# def CreateModel() -> Sequential:
#   model = tf.keras.models.Sequential()
#   model.add(tf.keras.layers.Dense(units = 1500, activation="relu"))
#   model.add(tf.keras.layers.Dense(units = 1024, activation="relu"))
#   model.add(tf.keras.layers.Dense(units = 512, activation="relu"))
#   model.add(tf.keras.layers.Dense(units = 128, activation="relu"))
#   model.add(tf.keras.layers.Dense(units = 32, activation="relu"))
#   model.add(tf.keras.layers.Dense(units = 6, activation="sigmoid"))
#   model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
#   return model

def CreateModel():
  model = tf.keras.models.Sequential()
  model.add(tf.keras.layers.Dense(units = 1500, activation="relu"))
  model.add(tf.keras.layers.Dense(units = 1024, activation="relu"))
  model.add(tf.keras.layers.Dense(units = 512, activation="relu"))
  model.add(tf.keras.layers.Dropout(rate = 0.2))
  model.add(tf.keras.layers.Dense(units = 128, activation="relu"))
  model.add(tf.keras.layers.Dense(units = 32, activation="relu"))
  model.add(tf.keras.layers.Dense(units = 6, activation="sigmoid"))
  model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
  return model

Model = CreateModel()
Model.load_weights("weights/TF_ONLY_MODEL")
print(Model)
# CV = None
# Encoder = None 

with open("TextEncoder.pkl", "rb") as f:
    text_encoder = pickle.loads(f.read())


def MakePred(ANN,s):
  string = [s]
  string = text_encoder.texts_to_matrix(string, mode="binary")
  pred = ANN.predict(string)
  # index = np.argmax(pred)
  print(string)
  print(pred)

MakePred(Model, "i had a terrible day today i was so sad.")

# def MakePred(ANN):
#     print(CV.__class__)
#     UserInput = input("> ")
#     string = np.array([UserInput]) 
#     print(ANN)
#     string = CV.transform(string).toarray()
#     print(string)
#     pred = ANN.predict(np.array([string]))
#     print(pred)

# MakePred(Model)






