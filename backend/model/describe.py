import openai

openai.api_key = "KEY HERE"

def evaluate_hospital_bill(bill_details: str) -> str:
    prompt = f"Is the following hospital bill overpriced? Please provide a yes or no answer, along with an explanation.\n\n{bill_details}\n"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    return answer

if __name__ == "__main__":
    bill_details = """
    Hospital Bill:
    - Room charges: $500 per day (3 days)
    - Doctor's fee: $1000
    - Medication: $300
    - Lab tests: $250
    - Miscellaneous: $150
    """
    
    evaluation = evaluate_hospital_bill(bill_details)
    print("Hospital bill evaluation:\n", evaluation)
