import pandas as pd
from fuzzywuzzy import process

df = pd.read_csv("./data.csv")

def get_closest_median_cost(search_term, dataframe):
    descriptions = dataframe['description'].tolist()
    best_match = process.extractOne(search_term, descriptions)
    matched_description, match_score = best_match

    if match_score >= 80:  # change threshold
        median_cost = dataframe[dataframe['description'] == matched_description]['median_cost'].iloc[0]
        return median_cost
    else:
        return None

# Example usage
search_string = 'fever'
result = get_closest_median_cost(search_string, df)

if result is not None:
    print(f"{result:.2f}")
else:
    print(f"No close match was found.")
