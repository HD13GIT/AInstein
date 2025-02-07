from pycoingecko import CoinGeckoAPI

class CryptoBot:
    def __init__(self):
        self.cg = CoinGeckoAPI()

    def get_crypto_price(self, coin_id):
        return self.cg.get_price(ids=coin_id, vs_currencies='usd')

    def get_crypto_market_data(self):
        return self.cg.get_global_market_data()

    def get_crypto_summary(self, coin_id):
        return self.cg.get_coin_by_id(coin_id)

    def get_market_trends(self):
        return self.cg.get_search_trending()