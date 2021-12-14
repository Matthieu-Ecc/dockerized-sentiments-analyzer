from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    negative = "Negative : " + str(sentiment_dict['neg']*100) + "%"
    neutral =  "Neutral : " + str(sentiment_dict['neu']*100) + "%"
    positive = "Positive : " + str(sentiment_dict['pos']*100) + "%"


    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
        return "Positive" , negative, neutral, positive
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")
        return "Negative" , negative, neutral, positive
    else :
        print("Neutral")
        return "Neutral", negative, neutral, positive
