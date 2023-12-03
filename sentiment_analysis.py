from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# reviews = open('tacos_reviews.txt')
reviews = open('ice_cream_reviews.txt')


for review in reviews:
    print('\n')
    print(review)
    sentiment_score = analyzer.polarity_scores(review)
    print(sentiment_score)
