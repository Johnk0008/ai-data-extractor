from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def extract_with_llm(text):
    prompt = f"""
    Extract product_name, price, quantity from below text in JSON format:
    
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content