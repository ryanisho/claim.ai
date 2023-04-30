from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from model.image_reader import read_image

df1 = pd.read_csv("model/data/data.csv")

# Function to find the closest match
def find_closest_match(billing_description, descriptions, threshold=0.3):
    vectorizer = TfidfVectorizer()
    descriptions_matrix = vectorizer.fit_transform(descriptions)
    query_vector = vectorizer.transform([billing_description])

    similarities = cosine_similarity(
        query_vector, descriptions_matrix).flatten()
    max_similarity = max(similarities)

    if max_similarity > threshold:
        closest_index = similarities.argmax()
        return descriptions[closest_index]
    else:
        return ''

# Function to find the description related to total charges
def find_total_charges_description(df):
    total_charges_rows = df[df['description'].str.contains('total', case=False, na=False, regex=False) |
                            df['description'].str.contains('sum', case=False, na=False, regex=False) |
                            df['description'].str.contains('aggregate', case=False, na=False, regex=False)].copy()
    if len(total_charges_rows) > 0:
        return total_charges_rows.iloc[0]['description']
    else:
        return ''

# Function to find the percent difference between two values
def percent_difference(value1, value2):
    difference = abs(value1 - value2)
    average = (value1 + value2) / 2
    percent_diff = (difference / average) * 100
    return percent_diff

# Function to get the price corresponding to a description
def get_price_for_description(df, target_description):
    result = df[df['description'] == target_description]

    if len(result) > 0:
        return result.iloc[0]['price']
    else:
        return None

def main(path):
    path = read_image(path)
    df2 = path

    # Combine all the descriptions in the new dataframe
    combined_description = ' '.join(path['description'].tolist())

    # Find the most related description in the original dataframe
    result = find_closest_match(combined_description, df1['description'].tolist())

    if result != '':
        if find_total_charges_description(df2) != '':
            known_median = get_price_for_description(df1, result)
            new_value = get_price_for_description(
                df2, find_total_charges_description(df2))
            if (percent_difference(known_median, new_value) > 30 and new_value > known_median):
                return ["The bill is priced higher than the NY state medians for diagnostic related group classifications", True]
            else:
                return ["The bill is reasonably priced according to NY state medians for diagnostic related group classifications", False]
    else:
        return "No close match was found."
