from yelpapi import YelpAPI 
import pandas as pd 

api_key = 'bhivYolP2EEOybI_SvFPfQzM2pfmUlj65JYFxxn7qeZzJBrb9hyHuLgc3NidmAvFTpnUu7l_jmQjzQT1mKkQ5ToxCrDYwxZ10XqeuxupWyerel_mi-UHBnaodeRMZXYx'

yelp_api_instance = YelpAPI(api_key)
search_term = 'pizza'
location_term = "El Paso, TX"

search_results = yelp_api_instance.search_query(
    term=search_term, location=location_term,
    sort_by = 'rating', limit =20
)

# print(search_results)

for business in search_results['businesses']:
    print('\n')
    print(business)

result_df = pd.DataFrame.from_dict(search_results['businesses'])

print(result_df)
result_df.to_csv('api_result.csv',index=False)

# id_for_reviews = 'little-habana-el-paso'

# reviews_response = yelp_api_instance.reviews_query(id=id_for_reviews)
# reviews_df = pd.DataFrame.from_dict(reviews_response['reviews'])
# reviews_df.to_csv('api_results.csv',index=False)

# for review in reviews_response['reviews']:
#     print('\n')
#     print(review)
