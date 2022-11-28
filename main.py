import time
import hashlib
from urllib.request import urlopen, Request


TIMER = 3
URL = 'https://toronto.craigslist.org/search/bia'


class Monitor:
    def __init__(self, url):
        self.url = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        self.response = None
        self.hash = None

    def _getResponse(self):
        return urlopen(self.url).read()

    def _getHash(self, response):
        return hashlib.sha224(response).hexdigest()
    
    def update(self):
        try:
            newResponse = self._getResponse()
            newHash = self._getHash(newResponse)
        except Exception as e:
            print(e)
        finally:
            if self.hash == newHash:
                print("Nothing changed.")
            else:
                print("Something changed.")
                self.hash = newHash        
                self.response = newResponse
                

if __name__ == '__main__':
    monitor = Monitor(URL)

    while True:
        monitor.update()
        time.sleep(2)


            
    
    




