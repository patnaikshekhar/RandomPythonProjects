import urllib
import json
import pymongo
import datetime



def getTwitterFeeds(searchString, noOfResults, maxValue):
    url = "http://search.twitter.com/search.json?q=" + searchString + "&rpp=" + str(noOfResults) + "&include_entities=true&result_type=recent&lang=en"

    if maxValue != None:
        url = url + "&since_id=" + str(maxValue[searchString.replace(" ", "") + "_max_id"])
    
    u = urllib.urlopen(url)
    object = json.loads(u.read())
    return object;

def storeFeedsForList(list):   
    conn = pymongo.Connection()
    db = conn.twitter_feeds

    for string in list:
        print "Working on String " + string
        print "___________________________________"
        count = 0
        key = string.replace(" ", "") + "_max_id"
        
        maxValue = None
        maxValue = db.maxId.find_one({key : {'$exists' : "true"}})

        print maxValue
        
        if maxValue != None:
            print "Getting values after " + str(maxValue[key])
        else:
            print "Starting first get"
            
        twitterFeed = getTwitterFeeds(string, 1000, maxValue)

        if len(twitterFeed["results"]) > 0:
            for result in twitterFeed["results"]:
                count = count + 1
                result["Queried On"] = str(datetime.datetime.now())
                result["Queried String"] = string
                db.results.insert(result)
                print str(count) + ". " + result["text"]

            print "Total Count : " + str(count)
            
            if maxValue == None:
                maxValue = dict()    
            maxValue[key] = twitterFeed["max_id"]
            db.maxId.save(maxValue)
            
            print "___________________________________"
        

