from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import image_reader as ir

df1 = pd.read_csv("backend\model\data\data.csv")
df2 = ir.read_image("backend\model\data\CSBill1.png")
df2 = pd.DataFrame(
    {"description": ["x-ray", "liver transplant", "medications : XYZ", "aggregated charges"],
     "price": [1109, 221580, 5000, 121000]})  # predefined for testing purposes

# Function to find the closest match


def find_closest_match(billing_description, descriptions, threshold=0.7):
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
    total_charges_rows = total_charges_rows[total_charges_rows['description'].str.contains(
        'charges', case=False, na=False, regex=False)]

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


def get_closest_match():
    return find_closest_match(combined_description, df1['description'].tolist())


# Combine all the descriptions in the new dataframe
combined_description = ' '.join(df2['description'].tolist())

# Find the most related description in the original dataframe
result = find_closest_match(combined_description, df1['description'].tolist())

if result != '':
    print(result)
    if find_total_charges_description(df2) != '':
        known_median = get_price_for_description(df1, result)
        new_value = get_price_for_description(
            df2, find_total_charges_description(df2))
        if (percent_difference(known_median, new_value) > 30 and new_value > known_median):
            # TODO: return this and send to front-end
            print("The bill is priced higher than the NY state medians for diagnostic related group classifications")
        else:
            # TODO: return this and send to front-end
            print("The bill is reasonably priced according to NY state medians for diagnostic related group classifications")
else:
    # TODO: return this and send to front-end
    print("No close match was found.")
