import pymongo
from decimal import *

score_finder = {"need": 4, "want": 3, "must have": 5, "good": 1,
                "nice": 2, "awesome": 2, "buy": 5, "cost": 1,
                "when": 1, "bad": -2, "hate": -10, "coupon": 3}


def getTopTweets(queried_string, threshold):
    conn = pymongo.Connection()
    db = conn.twitter_feeds

    score_list = []
    
    for tweet in db.results.find({'Queried String': queried_string}):
        tweet_score = 0
        for word in score_finder.keys():
            if word in tweet['text']:
                tweet_score += score_finder[word]

        if tweet_score >= threshold:
            score_list.append((tweet['text'], tweet_score))

    return score_list

def getScore(queried_string):
    conn = pymongo.Connection()
    db = conn.twitter_feeds

    score = 0
    no_of_tweets = 0
    
    for tweet in db.results.find({'Queried String': queried_string}):
        for word in score_finder.keys():
            if word in tweet['text']:
                score += score_finder[word]

        no_of_tweets += 1
        
    ratio = Decimal(score)/Decimal(no_of_tweets)
    
    return (score, no_of_tweets, round(ratio, 3))

def sort_score_array(key):
        return key[-1]

if __name__ == '__main__':
    for tweet in sorted(getTopTweets('Nexus 7', 7), key=sort_score_array,
                        reverse=True):
        print u'Tweet = {0}, Score = {1}'.format(tweet[0], tweet[1])

    """strings = ["Windows Phone", "iPhone", "Android", "Windows 8", "iPad Mini", "Nexus 7"]

    for string in strings:
        scores = getScore(string)
        print u'{0}, Score = {1}, Popularity = {2}, Increase = {3}'.format(
            string, scores[0], scores[1], scores[2])"""
    
    
