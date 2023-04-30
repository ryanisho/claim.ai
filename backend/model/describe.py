import openai
import pandas as pd
from model.anomaly import * 
from model.image_reader import read_image
import model.config 

openai.api_key = model.config.OPENAI_KEY

df1 = pd.read_csv("model/data/data.csv")

def describeMain(path):
    df2 = read_image(path)
    combined_description = ' '.join(df2['description'].tolist())
    condition = model.anomaly.find_closest_match(
        combined_description, df1['description'].tolist())

    if condition != '':
        # make a chat-bot request for a description
        description = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Describe {condition}. Provide a short list of symptoms, tests, and treatments in a paragraph format with no bulliten points.",
            max_tokens=400,
            n=1,
            stop=None,
            temperature=0.25,
        )
        f1 = description.choices[0].text

        list = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Describe {condition}. List 8 very-short microtransactions associated with hospitals that charge for this type of condition. Do not add any other information.",
            max_tokens=400,
            n=1,
            stop=None,
            temperature=0.25,
        )
        f2 = list.choices[0].text
        return [f1, f2]
    else:
        return None
