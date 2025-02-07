import openai

class GPT4Bot:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

    def generate_content(self, topic):
        prompt = f"Write a detailed and engaging post about {topic}."
        return self.generate_response(prompt)

    def analyze_sentiment(self, text):
        prompt = f"Analyze the sentiment of the following text and return 'positive', 'negative', or 'neutral': {text}"
        return self.generate_response(prompt)