import pandas as pd
from fuzzywuzzy import process

df = pd.read_csv("./data.csv")

def get_closest_description(search_term, dataframe):
    descriptions = dataframe['description'].tolist()
    best_match = process.extractOne(search_term, descriptions)
    matched_description, match_score = best_match

    if match_score >= 80:  # threshold level
        return matched_description
    else:
        return None

search_string = 'heart'
result = get_closest_description(search_string, df)

if result is not None:
    print(result)
else:
    print("No close match was found.")
