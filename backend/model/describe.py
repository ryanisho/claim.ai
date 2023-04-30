import openai
import anomaly
import pandas as pd
import image_reader as ir
openai.api_key = OPENAI_KEY

# define the medical condition/diagnostic category you want to analyze
condition_example = "heart disease"

df1 = pd.read_csv("backend\model\data\data.csv")
df2 = ir.read_image("backend\model\data\CSBill1.png")
df2 = pd.DataFrame(
    {"description": ["x-ray", "liver transplant", "medications : XYZ", "aggregated charges"],
     "price": [1109, 221580, 5000, 121000]})
combined_description = ' '.join(df2['description'].tolist())
condition = anomaly.find_closest_match(
    combined_description, df1['description'].tolist())


if condition != '':
    # make a chat-bot request for a description
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Describe {condition}. Provide a short list of symptoms, tests, and treatments. Also, provide a list of 10 or less microtransactions associated with hospitals that charge for this type of condition.",
        max_tokens=400,
        n=1,
        stop=None,
        temperature=0.25,
    )

    # print the generated text
    print(response.choices[0].text)  # TODO: return this and send to front-end
else:
    # TODO: return this and send to front-end
    print("Bill diagnostic category not recognized")
