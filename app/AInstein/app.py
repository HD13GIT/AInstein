from flask import Flask, request
from flask_limiter import Limiter
from twitter_integration import TwitterBot
from gpt_integration import GPT4Bot
from crypto_integration import CryptoBot
from blockchain_integration import BlockchainBot

app = Flask(__name__)
limiter = Limiter(app)

twitter_bot = TwitterBot("API_KEY", "API_SECRET_KEY", "ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
gpt_bot = GPT4Bot("OPENAI_API_KEY")
crypto_bot = CryptoBot()
blockchain_bot = BlockchainBot("API_KEY")

@app.route("/tweet", methods=["POST"])
@limiter.limit("10 per minute")
def tweet():
    message = request.json.get("message")
    twitter_bot.tweet(message)
    return "Tweet posted!", 200

@app.route("/reply", methods=["POST"])
@limiter.limit("10 per minute")
def reply():
    tweet_id = request.json.get("tweet_id")
    message = request.json.get("message")
    twitter_bot.reply_to_tweet(tweet_id, message)
    return "Replied to tweet!", 200

@app.route("/crypto_price", methods=["GET"])
def crypto_price():
    coin_id = request.args.get("coin_id")
    price = crypto_bot.get_crypto_price(coin_id)
    return price, 200

@app.route("/eth_transactions", methods=["GET"])
def eth_transactions():
    address = request.args.get("address")
    transactions = blockchain_bot.get_eth_transactions(address)
    return transactions, 200

if __name__ == "__main__":
    app.run(debug=True)