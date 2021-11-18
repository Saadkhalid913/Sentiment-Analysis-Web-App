import tensorflow as tf 
from tensorflow.keras.models import Sequential 
import re
import pickle 
import numpy as np 
import nltk
from nltk.stem import wordnet, WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download("wordnet")
nltk.download("stopwords")

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

emotions = ['anger', 'fear', 'joy', 'love', 'sadness', 'surprise']

@tf.autograph.experimental.do_not_convert
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


LEMMA = False
Model = CreateModel()
if not LEMMA:
  Model.load_weights("weights/TF_ONLY_MODEL")
else:
  Model.load_weights("LEMMA_WEIGHTS/MODEL_WITH_LEMMAS")

def GetStopwords():
  words = stopwords.words("english")
  words.remove("not")
  return words

EnglishStopwords = GetStopwords()


with open("TextEncoder.pkl", "rb") as f:
    text_encoder = pickle.loads(f.read())

def replace_not_alphabetical_chars(s: str):
  return re.sub("[^a-zA-Z]", " ", s)
def SplitSentence(s: str):
  s = s.lower()
  s = s.split()
  return s 

lemmatizer = WordNetLemmatizer()
def MakePred(s):
  sentence = replace_not_alphabetical_chars(s)  
  sentence = SplitSentence(sentence)
  # sentence = [word for word in sentence if word not in set(EnglishStopwords)]
  sentence = " ".join(sentence)
  string = [sentence]
  string = text_encoder.texts_to_matrix(string, mode="binary")
  pred = list(Model.predict(string)[0])
  pred = list(map(float, pred))
  return [{"name": emotions[i], "percentage": pred[i]} for i in range(len(emotions))]

if __name__ == "__main__":
  print(MakePred("Today I had a great day!"))





