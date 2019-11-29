import tweepy

import csv

from textblob import TextBlob

consumer_key='<YOUR CONSUMER KEY FROM TWITTER APIS>'
consumer_secret='<YOUR CONSUMER SECRET/PASSWORD FROM TWITTER APIS'
access_token='<YOUR ACCESS TOKEN FOR API>'
access_token_secret='<YOUR ACCESS TOKEN SECRET FOR API>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

positive = 0
total=0
negative = 0
neutral = 0
with open('persons.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile)
    for tweet in tweepy.Cursor(api.search, q="Narendra Modi", rpp=100, count=20, result_type="recent", include_entities=True, lang="en").items(200):
      if (not tweet.retweeted) and ('RT @' not in tweet.text):
        total = total+1
        polarity = 'neutral'
        #print('Tweet: ' + tweet.text)
        analysis = TextBlob(tweet.text)
        #print(analysis.sentiment)
        if(analysis.sentiment.polarity > 0.2):
          polarity='positive'
          positive = positive +1
        if(analysis.sentiment.polarity < -0.2):
          polarity= 'negative'
          negative = negative +1
        if(analysis.sentiment.polarity <0.2):
          if(analysis.sentiment.polarity > -0.2):
            neutral = neutral +1
        #print(polarity)
        filewriter.writerow([polarity, analysis.sentiment.polarity, tweet.text])
print("Total Results ", total)

cols = ['r', 'g', 'c']
lables = ['negative', 'positive', 'neutral']
data= [negative, positive, neutral]

import matplotlib.pyplot as plt
plt.pie(data, labels=lables, colors=cols)
plt.show()
