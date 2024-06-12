# 🎯 The general context and objectives of the project
This project aims to design and implement a sentiment analysis system leveraging artificial neural networks to process Twitter data. This field enables the automatic determination of opinions from collected text. By using deep learning techniques, particularly recurrent neural networks (RNNs) and long short-term memory (LSTM) units, our system is especially well-suited for handling textual sequences.

The primary objective of our project is to design a neural network model capable of classifying sentiments into different categories: 'Very Negative', 'Negative', 'Neutral', 'Positive', and 'Very Positive'. Our web application takes a keyword as input, searches for tweets associated with that keyword, and performs sentiment analysis on each tweet to eventually assess the overall sentiment regarding the topic.

![sentiment](https://github.com/HafsaTATA/Sentiment_analysis-App/assets/120058921/60f732b8-3e9e-472b-b8b6-c35d95911687)

#  	📊 Project progress: 
To illustrate the detailed planning of the project, here is the Gantt chart which presents the different stages and their schedule.
![Capture d'écran 2024-06-10 205521](https://github.com/HafsaTATA/Sentiment_analysis-App/assets/120058921/262f6ebf-ede3-449f-bd65-d97933b53a87)

# Functional Requirements:
- **Neural Network Creation:** Develop a process for creating a neural network to ensure optimal model design for sentiment analysis.
- **Neural Network Model Training:** Implement a mechanism for training the neural network using a diverse set of data to ensure accurate sentiment recognition.
- **Real-Time Sentiment Analysis:**  Develop a real-time analysis feature providing immediate feedback on the sentiment of analyzed tweets.
- **Adaptability to Various Scenarios:** Design the neural network model to be adaptable to different sentiment analysis scenarios, ensuring reliable performance with varying text types.
- **Performance Optimization:** Plan future model optimization to ensure fast and responsive performance for a smooth user experience.
- **Ease of Maintenance:**  Design a modular structure for the model to facilitate future maintenance and the addition of features without compromising simplicity of use.
# Non-Functional Requirements:
- **System Performance:** The system should provide real-time or near-real-time sentiment analysis results, minimizing tweet processing time for a smooth user experience.
- **Reliability:** Ensure reliable sentiment classification with minimized error rates, guaranteeing high consistency and accuracy in tweet analysis results.
- **Scalability:** Design the system to be scalable, allowing easy integration of new features and increased processing capacity as data volume grows.
- **Adaptability:** The neural network model should be adaptable to different hardware and software configurations, ensuring optimal performance across various platforms (servers, cloud, etc.).
- **Interfacing and Integration:** Provide APIs to facilitate integration with other systems and tools, ensuring smooth interaction and system extensibility.
# 📒 Essential Theoretical Principles
## Sentiment Analysis :basecampy:  :
Sentiment Analysis, also known as opinion mining, is a subfield of Natural Language Processing (NLP) that focuses on identifying and extracting subjective information from text data. It involves determining the sentiment or emotion expressed in a piece of text, such as a tweet, review, or comment.

It consists of 5 key steps:

![Capture d'écran 2024-06-12 164225](https://github.com/HafsaTATA/Sentiment_analysis-App/assets/120058921/224e2633-9323-4027-86eb-1da74c2df339)

- The first two stages focus on data management, while the last three stages focus on creating and training the sentiment classification model.
1. **Data Extraction:**

This step involves collecting data, including tweets, which will be useful to us as training, testing and validation data. We collected data from two main sources: `Twitter` and `Kaggle`. For Twitter, we extracted tweets using our Python code and different libraries. For Kaggle, we downloaded ready-to-use datasets.

2. **Preprocessing:**

   ![Capture d'écran 2024-06-12 165149](https://github.com/HafsaTATA/Sentiment_analysis-App/assets/120058921/49d0b093-b2d4-4c00-a2f0-10317ffb8e9a)

- Once the data is collected, it needs to be cleaned and prepared. This includes converting texts to lowercase, removing non-text elements (mentions, hashtags, URLs, html tags), processing chat words, removing characters specials and punctuations, spelling correction, Stemming and lemmatization and filtering of stop words.
```
❤️Stemming involves cutting prefixes or suffixes to obtain the root word (for example, “jumping” becomes “jump”). Lemmatization, on the other hand, reduces words to their dictionary or base form (e.g., “better” becomes “good”).

❤️Stop words are common words such as "the", "and", "in", which appear frequently in the language but often do not carry much sentimental information
```
  - Tokenization is an NLP task which consists of dividing a piece of text into smaller units called “tokens”. These tokens are either sentences, words or characters. In our project, we use tokenization of sentences into words, as shown in Figure.
3. **Sentiment Identification:**

   At this stage, the preprocessed text data is passed through the neural network to extract and identify the sentiments present in the texts. tq it analyzes sequences of words to detect patterns indicative of specific feelings.
   
4. **Feature Selection:**

  Once the sentiments have been identified, we then move on to selecting the most relevant textual features to train the classification model. For this reason, we used techniques such as Word Embedding encoding in order to transform the textual data into vectors of reduced dimensions (100) which capture the semantic relationships between words. ie words used in similar contexts will have close vectors in vector space.
   
5. **Sentiment Classification:**

   In this last step, the text data, transformed into vectors, is used to train the model. The neural network, trained on this data annotated with sentiment labels, learns to predict the sentiments of new tweets.

## Model architecture :basecampy: :

![Capture d'écran 2024-06-12 165736](https://github.com/HafsaTATA/Sentiment_analysis-App/assets/120058921/f381cc91-8816-42b2-9c2f-48d1f6057977)

We opted for an LSTM (Long Short-Term Memory) type model for several reasons:
- **Sequence Management:** LSTMs are particularly suitable for managing sequential and textual data, such as in our case tweets, because they can capture long-term dependencies in sequences.
- **Gradient Vanishing Prevention:** LSTMs are designed to overcome the problem of gradient vanishing, allowing them to retain relevant information over long sequences of text.

### We designed our model with several layers to capture essential characteristics of tweets and improve model performance:
🔸**Embedding Layer:** The Embedding Layer transforms the words of our text into vectors of fixed dimensions. Each word is represented by a dense vector of size 100. This transformation makes it possible to capture semantic relationships between words, thus facilitating their processing by subsequent layers. Similar words will have similar vectors.

🔸**LSTM Layer:** The Long Short-Term Memory (LSTM) layer is a type of recurrent neural network (RNN) capable of capturing long-term dependencies in text sequences. It uses 64 units. The dropout=0.5 parameter applies a dropout (50%) on the input connections to avoid overfitting. The recurrent_dropout=0.5 parameter applies a dropout (50%) on internal recurring connections of the LSTM.

LSTMs are well suited for processing sequential data and can retain important information across long sequences, which is crucial for context-based sentiment analysis.

🔸**Batch Normalization:** Batch normalization normalizes the activations of the previous layer, thereby stabilizing and accelerating learning.

🔸**Dropout:** The Dropout layer introduces a 40% dropout rate, randomly disabling units from the previous layer during each stage of training. This helps prevent overfitting by forcing the model to learn more robust representations that do not depend on the activation of certain specific units.

🔸**Dense(5, activation="sigmoid"):** The output layer has 5 units with sigmoid activation, corresponding to the 5 sentiment classes. Sigmoid activation is used because it outputs probabilities for each class.

# Visualisation:
### Landing page:

![Capture d'écran 2024-06-03 004624](https://github.com/HafsaTATA/Sentiment_analysis-App/assets/120058921/b443f213-4186-4a85-b67f-8134c52f8430)

### Dashboard:

![negative1](https://github.com/HafsaTATA/Sentiment_analysis-App/assets/120058921/77763a40-5b63-4a75-b10c-6415a566bc82)

![negativee2](https://github.com/HafsaTATA/Sentiment_analysis-App/assets/120058921/342b2452-f78b-4b6e-9092-fc7418329d3c)

![NEGATIVE3](https://github.com/HafsaTATA/Sentiment_analysis-App/assets/120058921/5e6deb94-d2c0-4593-ab9c-fad6243cec51)

![NEGATIVE4](https://github.com/HafsaTATA/Sentiment_analysis-App/assets/120058921/ebbc0a1b-8b72-4ee3-aa10-e5c2f3a68521)

![NEGATIVE5](https://github.com/HafsaTATA/Sentiment_analysis-App/assets/120058921/d334f03f-de41-44f3-9303-9247cb672f9b)


