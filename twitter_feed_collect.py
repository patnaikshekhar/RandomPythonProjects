import twitter_feed_get_generic as twitter
import time

while(1):
    print "Start : %s" % time.ctime()
    try:
        twitter.storeFeedsForList(["Windows Phone", "iPhone", "Android", "Deloitte", "IBM", "Accenture", "Windows 8", "OS X", "Ubuntu", "Oracle", "Lady Gaga", "Justin Bieber", "Katy Perry", "Barack Obama", "iPad Mini", "Nexus 7"])
    except:
        print "Error occurred recovering...."
    time.sleep(60)
    print "End : %s" % time.ctime()
