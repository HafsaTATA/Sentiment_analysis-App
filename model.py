import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from nltk.corpus import stopwords

from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, TransformerMixin

from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, BatchNormalization, Dropout
import os
import re
import string
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint

import nltk
nltk.download('stopwords')
data_train = pd.read_excel("./Training_dataset.xlsx")
data_test = pd.read_excel("./test_dataset.xlsx")
data_val = pd.read_excel("./Validation_dataset.xlsx")

data_train = data_train.drop(columns = ["Date","Lang","Likes","Retweets","URL","Replies"])
data_val = data_val.drop(columns=["Date", "Lang", "Likes", "Retweets", "URL", "Replies"])
data_test = data_test.drop(columns = "ItemID")

data = pd.concat([data_train, data_test]).reset_index(drop=True)
data = data.sample(frac = 1).reset_index(drop = True)
##Nettoyage des données
class CleanText(BaseEstimator, TransformerMixin):
    def remove_html_tags(self, input_text):
        pattern = re.compile('<.*?>')
        return pattern.sub(r'', input_text)

    def remove_mentions(self, input_text):
        return re.sub(r'@\w+', '', input_text)

    def remove_urls(self, input_text):
        return re.sub(r'((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)', '', input_text)

    def emoji_oneword(self, input_text):
        return input_text.replace('_','')

    def remove_punctuation(self, input_text):
        punct = string.punctuation
        trantab = str.maketrans(punct, len(punct)*' ')
        return input_text.translate(trantab)

    def remove_digits(self, input_text):
        return re.sub('\d+', '', input_text)

    def to_lower(self, input_text):
        return input_text.lower()

    def remove_stopwords(self, input_text):
        stopwords_list = stopwords.words('english')
        whitelist = ["n't", "not", "no"]
        words = input_text.split()
        clean_words = [word for word in words if (word not in stopwords_list or word in whitelist) and len(word) > 1]
        return " ".join(clean_words)

    def stem_words(self, input_text):
        words = input_text.split()
        stemmed_words = [self.stemmer.stem(word) for word in words]
        return " ".join(stemmed_words)

    def fit(self, X, y=None, **fit_params):
        return self

    def transform(self, X, **transform_params):
        clean_X = X.apply(self.remove_html_tags).apply(self.remove_mentions).apply(self.remove_urls).apply(self.emoji_oneword).apply(self.remove_punctuation).apply(self.remove_digits).apply(self.to_lower).apply(self.remove_stopwords)
        return clean_X
ct = CleanText()
data['Text'] = data['Text'].fillna('')
data_val['Text'] = data_val['Text'].fillna('')

data['Text'] = ct.fit_transform(data['Text'])
data_val['Text'] = ct.fit_transform(data_val['Text'])
## Diviser les données : Train/ Test
X_train, X_test, y_train, y_test = train_test_split(data.drop("sentiment", axis=1),
                                                    data.sentiment,
                                                    test_size=0.2,
                                                    random_state=888)

X_train = X_train.Text.values
y_train = y_train.values
X_test = X_test.Text.values
y_test= y_test.values
## Diviser les données de validation
X_val, X_trainn, y_val, y_trainn = train_test_split(data_val.drop("sentiment", axis=1),
                                                    data_val.sentiment,
                                                    test_size=1,
                                                    random_state=888)
token = Tokenizer()
token.fit_on_texts(data_val)
max_length_val = max([len(word.split()) for word in data_val])

X_val = X_val.Text.values
y_val = y_val.values

X_val_token = token.texts_to_sequences(X_val)
X_val = pad_sequences(X_val_token, maxlen=max_length_val, padding="post")
##word embedding
total_tweets = np.concatenate((X_train, X_test), axis=0)
token = Tokenizer()
token.fit_on_texts(total_tweets)
max_length = max([len(word.split()) for word in total_tweets])
vocabulary_dim = len(token.word_index) + 1

X_train_token = token.texts_to_sequences(X_train)
X_test_token = token.texts_to_sequences(X_test)

X_train = pad_sequences(X_train_token, maxlen=max_length, padding="post")
X_test = pad_sequences(X_test_token, maxlen=max_length, padding="post")
##création du modele
model = Sequential()
model.add(Embedding(input_dim=vocabulary_dim,  output_dim=100, input_length=max_length))
model.add(LSTM(units=64, dropout=0.5, recurrent_dropout=0.5))
model.add(Dense(32, activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Dense(16, activation="relu"))
model.add(BatchNormalization())
model.add(Dense(5, activation="sigmoid"))
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"], run_eagerly=True)

print(model.summary())
y_train = to_categorical(y_train, num_classes=5)
y_val = to_categorical(y_val, num_classes=5)

checkpoint2 = ModelCheckpoint("rnn_model.hdf5", monitor='val_accuracy', verbose=1,save_best_only=True, mode='auto', period=1,save_weights_only=False)
## Fitting the model
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=5, batch_size=512, callbacks=[checkpoint2])
model.save("twitter_project.h5")