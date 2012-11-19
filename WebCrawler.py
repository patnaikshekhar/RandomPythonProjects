import urllib
import re
import sys
import os

def grabData(downloadURL, URLPath, PagesPath, doneURLs):
    try:
        #Initilize the URLs which have been completed
        if not doneURLs:
            doneURLs = []
        
        #Open URL and Read Lines
        if not (downloadURL in doneURLs):
            doneURLs.append(downloadURL)
            url_list = []
            print "Downloading from URL : " + downloadURL
            url = urllib.urlopen(downloadURL)
            fileName = downloadURL.replace(":", "_").replace("\\", "_").replace("/", "_").replace("?", "_").replace("=", "_").replace("&", "_") + ".html"
            f = open(os.path.join(PagesPath, fileName), 'w')
            f.write("<!--" + downloadURL + "-->")
            for line in url:
                f.write(line + "\n")
                match = re.search(r'<a\s+?href\s*=\s*?"(.+?)"', line)
                if match:
                    new_url = match.group(1)
                    """if new_url[0] == '/':
                        if downloadURL[-1] == '/':
                            new_url = downloadURL + new_url[1:]
                        else:
                            new_url = downloadURL + new_url"""
                    url_list.append(new_url)
            f.close()
            
            #Write URLs to URL File
            print "Writing URLs to file"
            f = open(os.path.join(URLPath, "URLList.txt") , 'a')

            for url in url_list:
                f.write(url + "\n")
                
            f.close()

            #For each URL Grab Data
            for url in url_list:
                print "Next URL : " + url
                grabData(url, URLPath, PagesPath, doneURLs)
        else:
            print "Skipping URL : " + downloadURL
    except:
        e = sys.exc_info()
        print "Error Occured : " + str(e)
    return

def main():
    #grabData("http://www.nytimes.com", "C:\Users\shpatnaik\Crawler", "C:\Users\shpatnaik\Crawler\Pages", None)
    #grabData("http://timesofindia.indiatimes.com/", "C:\Users\shpatnaik\Crawler", "C:\Users\shpatnaik\Crawler\Pages", None)
    grabData("http://deloittenet.com/", "C:\Users\shpatnaik\Crawler", "C:\Users\shpatnaik\Crawler\Pages", None)

if __name__ == '__main__':
    main()
