from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# function to print sentiments
# of the sentence.

# import sys

# input = sys.argv

# input[0]=""

# sentence = " ".join(input)



def sentiment_scores(sentence):
# Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
# polarity_scores method of SentimentIntensityAnalyzer
# oject gives a sentiment dictionary.
# which contains pos, neg, neu, and compound scores.

    sentiment_dict = sid_obj.polarity_scores(sentence)
    negative = ""+sentiment_dict['neg']*100 + "% Negative"
    neutral = ""+sentiment_dict['neu']*100 + "% Neutral"
    positive = ""+sentiment_dict['pos']*100 + "% Positive"

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


# while(True):

#     sentence = input('write a sentence for analyse \n')

#     sentiment_scores(sentence)

#     choice = input('do you want to continue y/n \n')

#     if choice != 'y':
#         break