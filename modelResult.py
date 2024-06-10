import pandas as pd
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# Assuming the `ct` (CleanText instance) and `token` (Tokenizer) are already defined as in your original code

# Step 1: Load the Trained Model
model = load_model("rnn_model.hdf5")

# Step 2: Prepare the Data
new_tweets = pd.read_excel("new_tweets.xlsx")
new_tweets['Text'] = new_tweets['Text'].fillna('')

# Clean the tweets
new_tweets['Text'] = ct.transform(new_tweets['Text'])

# Tokenize and pad the sequences
new_tweets_sequences = token.texts_to_sequences(new_tweets['Text'].values)
max_length = max([len(x.split()) for x in new_tweets['Text'].values])  # Ensure max_length is defined
new_tweets_padded = pad_sequences(new_tweets_sequences, maxlen=max_length, padding="post")

# Step 3: Predict Sentiments
predicted_probabilities = model.predict(new_tweets_padded)
predicted_classes = predicted_probabilities.argmax(axis=-1)

# Step 4: Store Results in a List of Dictionaries
results = []

for i, tweet in new_tweets.iterrows():
    result = {
        "Text": tweet['Text'],
        "Sentiment_Probabilities": predicted_probabilities[i],
        "Predicted_Sentiment": predicted_classes[i]
    }
    results.append(result)

# Example of accessing the results
for result in results:
    print(result)
