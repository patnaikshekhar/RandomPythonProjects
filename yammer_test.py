import urllib2
import urllib

foo_url = "https://www.yammer.com/api/v1/messages.json?access_token=T9cMsauXYehK4nmuD8boNg"
data = {'body': 'Another test message to yammer'}
data = urllib.urlencode(data)
print urllib2.urlopen(foo_url, data).read()
    
