import tweepy

class TwitterBot:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        self.auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def tweet(self, message, image_path=None):
        if image_path:
            media = self.api.media_upload(image_path)
            self.api.update_status(status=message, media_ids=[media.media_id])
        else:
            self.api.update_status(message)

    def reply_to_tweet(self, tweet_id, message):
        self.api.update_status(status=message, in_reply_to_status_id=tweet_id)

    def get_latest_tweets(self, hashtag, count=10):
        return self.api.search_tweets(q=hashtag, count=count)

    def get_trending_topics(self, location_id=1):
        trends = self.api.get_place_trends(location_id)
        return [trend['name'] for trend in trends[0]['trends']]