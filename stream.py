from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s


#consumer key, consumer secret, access token, access secret.
ckey="6b3Jt64mpb5vRjH73VufQfiYE"
csecret="TSb1hZyIZ527bTl5iOKZEcN0fwRbNAv08VJUvPEFZN5GBjA326"
atoken="4772832541-QD4gTzk8OIZwfvAvPKYvNsTwy0oZ0dOLQ4WS2ru"
asecret="CccfgqZKjY8GuXjx4QqcQFrujFZfhr2wxApaoELN2MsIv"

class listener(StreamListener):

    def on_data(self, data):

        all_data = json.loads(data)

        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Modi"])


 
