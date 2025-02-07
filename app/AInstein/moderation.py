class ModerationBot:
    def __init__(self):
        self.bad_words = ["scam", "fraud", "fake"]

    def check_content(self, text):
        for word in self.bad_words:
            if word in text.lower():
                return False
        return True

    def source_attribution(self, text):
        return f"Source: {text}"

    def fact_check(self, statement):
        # Placeholder for fact-checking API integration
        return f"Fact-checking result for: {statement}"