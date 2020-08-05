import tweepy
import json


class CalorieMateLIQUID:
    def __init__(self):
        config = json.load(open('config.json', 'r'))
        auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
        auth.set_access_token(config["access_token_key"], config["access_token_secret"])

        self.twitter = tweepy.API(auth)
        self.account = "CalorieMate_jp"
        self.tweet = "1290090004413181952"

    def follow(self, screen_name):
        try:
            self.twitter.create_friendship(screen_name)
            print(screen_name + " さんをフォローしました。")
        except tweepy.error.TweepError:
            print("Follow error")

    def retweet(self, id):
        try:
            self.twitter.retweet(id)
            print("リツイートしました。")
        except tweepy.error.TweepError:
            print("Retweet error")

    def wish(self, message="頼むから当たってくれ"):
        print(message)
