import urllib
import json
import pymongo
import datetime



def getTwitterFeeds(searchString, noOfResults, maxValue):
    url = "http://search.twitter.com/search.json?q=" + searchString + "&rpp=" + str(noOfResults) + "&include_entities=true&result_type=recent&lang=en"

    if maxValue != None:
        url = url + "&since_id=" + str(maxValue["max_id"])
    
    u = urllib.urlopen(url)
    object = json.loads(u.read())
    return object;

conn = pymongo.Connection()
db = conn.tutorial

maxValue = db.maxId.find_one({'max_id' : {'$ne' : 0}})

if maxValue != None:
    print "Getting values after " + str(maxValue["max_id"])
else:
    print "Starting first get"
    
twitterFeed = getTwitterFeeds("deloitte", 1000, maxValue)

if len(twitterFeed["results"]) > 0:
    for result in twitterFeed["results"]:
        result["Queried On"] = str(datetime.datetime.now())
        db.results.insert(result)
        print result["text"]

    if maxValue == None:
        maxValue = dict()    
    maxValue["max_id"] = twitterFeed["max_id"]
    db.maxId.save(maxValue)
    


