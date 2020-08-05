from calorie_mate_liquid import CalorieMateLIQUID

this = CalorieMateLIQUID()
follow = this.follow
retweet = this.retweet
wish = this.wish


def GetGoods():
    follow(this.account)
    retweet(this.tweet)
    wish()  # or you can use this function like: wish("当たりますように")


GetGoods()
