from yelpapi import YelpAPI
import pandas as pd
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


api_key = 'bhivYolP2EEOybI_SvFPfQzM2pfmUlj65JYFxxn7qeZzJBrb9hyHuLgc3NidmAvFTpnUu7l_jmQjzQT1mKkQ5ToxCrDYwxZ10XqeuxupWyerel_mi-UHBnaodeRMZXYx'
yelp_api = YelpAPI(api_key)
search_term = "ramen"
location_term = "El Paso, TX"
search_results = yelp_api.search_query(
    term=search_term, location=location_term,
    sort_by='rating', limit=20, offset=20)
# print(search_results)

# Converting list to df to select a restaruant for reviews
result_df = pd.DataFrame.from_dict(search_results['businesses'])
print(result_df)
# result_df.to_csv('code_10.csv')

# search for reviews in kees-teriyaki-and-sushi-el-paso

id_for_reviews = 'kaedama-el-paso'
reviews_response = yelp_api.reviews_query(id=id_for_reviews)


# converting the reviwes to Pandas Df
result_df = pd.DataFrame.from_dict(reviews_response['reviews'])
print(result_df)
# result_df.to_csv(f'{id_for_reviews}_kees_results.csv',index=False)
for review in reviews_response['reviews']:
    print('\n')
    print(review)

analyzer = SentimentIntensityAnalyzer()

reviews = open('code_10/kaedama-el-paso_kees_results.txt')


for review in reviews:
    print('\n')
    print(review)
    sentiment_score = analyzer.polarity_scores(review)
    print(sentiment_score)