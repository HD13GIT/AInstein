import requests

class BlockchainBot:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_eth_transactions(self, address):
        url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&apikey={self.api_key}"
        response = requests.get(url)
        return response.json()

    def get_eth_balance(self, address):
        url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={self.api_key}"
        response = requests.get(url)
        return response.json()

    def get_solana_transactions极速赛车onents** and **filepaths** as per the project plan. You can now run the application effortlessly. Let me know if you need further assistance! 🚀.
                        Respond ONLY with valid JSON."