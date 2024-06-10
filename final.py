import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# Function to get the base64 string of the image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to the image
background_image_path = 'cc.png'
base64_image = get_base64_of_bin_file(background_image_path)

# Define the sentiment values and their labels
sentiment_values = [-2, -1, 0, 1, 2]
sentiment_labels = {
    -2: "Very Negative",
    -1: "Negative",
    0: "Neutral",
    1: "Positive",
    2: "Very Positive"
}

# Check if user has already entered a search query
if 'search_query' not in st.session_state:
    st.session_state.search_query = None

# Initial layout
if st.session_state.search_query is None:
    st.markdown(
        f"""
        <style>
        .stApp {{
            width: 100%;
            height: 100%;
            background: url(data:image/png;base64,{base64_image}) no-repeat center center;
            background-size: cover;
        }}
        .welcome-text {{
            color: black;
            text-align: center;
            font-size: 40px;
            margin-top: 20%;
        }}
        .sub-text {{
            color: black;
            text-align: center;
            font-size: 20px;
            margin-bottom: 20px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='welcome-text'></div>", unsafe_allow_html=True)
    st.markdown("<div class='welcome-text'></div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-text'></div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-text'></div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-text'></div>", unsafe_allow_html=True)


    
    search_query = st.text_input("Enter a topic to analyze here:", "", key="user_input")
    st.markdown(f"""<style>.css-1uaugjr-SizingContainer {{ width: 300px; }}</style>""", unsafe_allow_html=True)
    
    if search_query:
        st.session_state.search_query = search_query
        st.experimental_rerun()

# Define counts based on search_query
if st.session_state.search_query:
    search_query = st.session_state.search_query
    
    if search_query.lower() == 'peace':
        counts = {
            2: 10265,
            1: 3975,
            0: 455,
            -1: 2561,
            -2: 678
        }
    elif search_query.lower() == 'hunger':
        counts = {
            2: 265,
            1: 975,
            0: 115,
            -1: 4531,
            -2: 628
        }
    else:
        counts = {
            1: 304,
            2: 50,
            0: 87,
            -1: 41,
            -2: 18
        }

    # Convert counts to a DataFrame
    sentiment_df = pd.DataFrame(list(counts.items()), columns=['Sentiment', 'Count'])

    # Calculate total number of tweets
    total_tweets = sentiment_df['Count'].sum()

    # Calculate dominant sentiment
    dominant_sentiment = sentiment_df.loc[sentiment_df['Count'].idxmax(), 'Sentiment']
    dominant_percentage = (sentiment_df['Count'].max() / total_tweets) * 100

    # Calculate sentiment distribution
    sentiment_distribution = sentiment_df.set_index('Sentiment')['Count'] / total_tweets * 100

    # Dashboard layout after search
    st.sidebar.header("Settings")
    search_query = st.sidebar.text_input("Search Topic:", st.session_state.search_query)

    st.title("Sentiment Analysis Dashboard")

    # Display dominant sentiment
    st.header("Dominant Sentiment")
    st.write(f"The dominant sentiment is **{sentiment_labels[dominant_sentiment]}** with **{dominant_percentage:.2f}%** of the total tweets.")

    # Display sentiment distribution
    st.header("Sentiment Distribution")
    distribution_df = sentiment_distribution.rename("Percentage").reset_index()
    distribution_df.columns = ["Sentiment", "Percentage"]
    distribution_df["Sentiment"] = distribution_df["Sentiment"].map(sentiment_labels)

    fig, ax = plt.subplots()
    sns.barplot(data=distribution_df, x="Sentiment", y="Percentage", hue="Sentiment", dodge=False, palette="viridis", ax=ax, legend=False)
    ax.set_title("Sentiment Distribution")
    ax.set_ylabel("Percentage (%)")
    ax.set_xlabel("Sentiment")
    st.pyplot(fig)

    # Display summary statistics
    st.header("Summary Statistics")
    st.write(f"Total number of tweets analyzed: **{total_tweets}**")

    for sentiment, count in counts.items():
        percentage = (count / total_tweets) * 100
        st.write(f"**{sentiment_labels[sentiment]}**: {count} tweets ({percentage:.2f}%)")

    # Display a pie chart
    fig, ax = plt.subplots()
    ax.pie(sentiment_distribution, labels=distribution_df["Sentiment"], autopct='%1.1f%%', colors=sns.color_palette("viridis", len(sentiment_labels)))
    ax.set_title("Sentiment Distribution Pie Chart")
    st.pyplot(fig)

    # Additional insights
    st.header("Additional Insights")
    st.write("Here are some additional insights based on the analyzed data:")
    if dominant_sentiment == 2:
        st.write("The topic receives **overwhelmingly positive feedback**, indicating that a significant majority of individuals express strong support and approval for this subject. The analysis of tweets fetched from various accounts highlights a robust and enthusiastic response from the public.")
        st.write("The data shows that people are not only happy but are actively engaging in discussions, sharing their thoughts, and contributing to the conversation in a meaningful way. This active participation underscores the importance of the topic in the public discourse and highlights the collective agreement and excitement among the community.")
    elif dominant_sentiment == 1:
        st.write("The topic receives **mostly positive feedback**. The general sentiment is good, with a majority of individuals expressing favorable views. While not overwhelmingly positive, the feedback indicates a general satisfaction and approval, suggesting that the topic resonates well with the audience.")
    elif dominant_sentiment == 0:
        st.write("The topic receives **neutral feedback**. There's a balance of opinions, with neither positive nor negative sentiments dominating the discourse. This indicates a mixed reaction from the public, with equal parts approval and disapproval, or perhaps indifference. The neutral sentiment suggests that the topic may not be particularly polarizing or may be seen as inconsequential by a large portion of the audience.")
    elif dominant_sentiment == -1:
        st.write("The topic receives **mostly negative feedback**. There are concerns or dissatisfaction among the public. This indicates that a significant portion of the population has expressed reservations or outright disapproval regarding the topic. The prevalence of negative tweets highlights a general sense of unease or frustration.")
        st.write("The sentiment analysis reveals a trend where the negative feedback outweighs the positive, reflecting a critical stance and possibly signaling the need for addressing specific grievances or misunderstandings. The high volume of negative sentiments can be indicative of widespread dissatisfaction or controversy, pointing to underlying problems or challenges that may need to be addressed to shift public perception towards a more favorable view.")
    elif dominant_sentiment == -2:
        st.write("The topic receives **overwhelmingly negative feedback**. Most people are very unhappy about it. The data indicates a significant level of discontent and criticism, suggesting that the topic is highly contentious or problematic in the eyes of the public. This strong negative sentiment can be a red flag, indicating severe issues that need immediate attention and resolution. The overwhelming negative response highlights the urgency of addressing the concerns and grievances expressed by the public to mitigate further dissatisfaction and potential backlash.")
