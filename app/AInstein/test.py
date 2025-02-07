import unittest
from twitter_integration import TwitterBot
from gpt_integration import GPT4Bot
from crypto_integration import CryptoBot
from blockchain_integration import BlockchainBot
from moderation import ModerationBot

class TestAInstein(unittest.TestCase):
    def test_twitter_bot(self):
        bot = TwitterBot("API_KEY", "API_SECRET_KEY", "ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
        self.assertIsNotNone(bot)

    def test_gpt_bot(self):
        bot = GPT4Bot("OPENAI_API_KEY")
        response = bot.generate_response("Hello, world!")
        self.assertIsInstance(response, str)

    def test_crypto_bot(self):
        bot = CryptoBot()
        price = bot.get_crypto_price("bitcoin")
        self.assertIsNotNone(price)

    def test_blockchain_bot(self):
        bot = BlockchainBot("API_KEY")
        transactions = bot.get_eth_transactions("0xaddress")
        self.assertIsNotNone(transactions)

    def test_moderation_bot(self):
        bot = ModerationBot()
        is_clean = bot.check_content("This is a scam!")
        self.assertFalse(is_clean)

if __name__ == "__main__":
    unittest.main()