# CalorieMateLIQUID
Python版

カロリーメイトのキャンペーンに応募する  
[#うちこむ人にバランス栄養](https://twitter.com/hashtag/%E3%81%86%E3%81%A1%E3%81%93%E3%82%80%E4%BA%BA%E3%81%AB%E3%83%90%E3%83%A9%E3%83%B3%E3%82%B9%E6%A0%84%E9%A4%8A)  
[#カロリーメイトリキッド](https://twitter.com/hashtag/%E3%82%AB%E3%83%AD%E3%83%AA%E3%83%BC%E3%83%A1%E3%82%A4%E3%83%88%E3%83%AA%E3%82%AD%E3%83%83%E3%83%89)

[JavaScript版](https://github.com/BonyChops/CalorieMateLIQUID)

![calorie_mate](caloriemate.jpeg)

[CalorieMate to Programmer](https://www.otsuka.co.jp/cmt/to_programmer/)

## Requirements
- Tweepy


```bash
conda install -c conda-forge tweepy 
```

or

```bash
pip install tweepy
```

- Twitter Developer Account (取得は[developer.twitter.com](https://developer.twitter.com/) から)
    - 申請方法などは[ここ](https://www.itti.jp/web-direction/how-to-apply-for-twitter-api/)を参照

## Usage
1. `config.json`を編集する。
```
{
    "consumer_key": "***",
    "consumer_secret": "***",
    "access_token_key": "***",
    "access_token_secret": "***"
}
```
2. `app.py`を実行
```bash
python app.py
```