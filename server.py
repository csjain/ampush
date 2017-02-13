'''
Created on Feb 10, 2017
@author: anujjain
'''

from random import randint
from tornado import ioloop, web
import json
from json import JSONEncoder


def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__


class SummaryBean(JSONEncoder):
    def __init__(self,utm,page,count):
        self.utm = utm
        self.page=page
        self.count = count

class SummaryHandler(web.RequestHandler):
    
    '''
    This class shows summary of web page hits.
    '''        
    def get(self):
        try:
            self.write(open("summary.html").read())
        except Exception as exc:
            self.write({"error":str(exc)})

class AjaxSummaryJsonHandler(web.RequestHandler):
    
    '''
    It handles REST url for /summaryJson
    '''    
    def get(self):
        try:
            self.write(Tracker.getSummaryJson())
        except Exception as exc:
            self.write({"error":str(exc)})

class TrackingHandler(web.RequestHandler):
    '''
    It handles REST url for /track
    '''    
    
    def get(self):
        try:
            utm_id = self.get_argument("utm_id")
            page = self.get_argument("page")
            Tracker.track(utm_id, page)
            self.write({"success":"true"})
        except Exception as exc:
            self.write({"error":str(exc)})            
            
class Tracker:
        
    '''
    This class acts as Tracker
    It handles tracking and gives back the summary
    '''    

    
    __web_page_track = {}
    __instance = None
    
    @staticmethod
    def getInstance():
        if not Tracker.__instance:
            Tracker.__instance = Tracker()
        return Tracker.__instance

    @staticmethod        
    def track(utm_id,page):
        if utm_id not in Tracker.getInstance().__web_page_track:
            Tracker.getInstance().__web_page_track[utm_id] = {}
        if page not in Tracker.getInstance().__web_page_track[utm_id]:
            Tracker.getInstance().__web_page_track[utm_id][page] = 0
        Tracker.getInstance().__web_page_track[utm_id][page] += 1
            
    @staticmethod
    def getSummaryJson():
        results = []
        for utm in Tracker.getInstance().__web_page_track:
            for page in Tracker.getInstance().__web_page_track[utm]:
                results = results + [SummaryBean(utm,page,Tracker.getInstance().__web_page_track[utm][page])]
        return json.dumps(results,default=dumper)
    
    @staticmethod
    def getScore(givenutm,givenpage):
        total = 0
        if givenutm not in Tracker.getInstance().__web_page_track:
            return 0;
        if givenpage not in Tracker.getInstance().__web_page_track[givenutm]:
            return 0;
        for page in Tracker.getInstance().__web_page_track[givenutm]:
            total += Tracker.getInstance().__web_page_track[givenutm][page]
        return (Tracker.getInstance().__web_page_track[givenutm][givenpage] / total) * 100
        
    
    
class Server(web.RequestHandler):
    
    '''
    This class acts as server.
    python -m server
    '''    
    
    web_page_dict = {"1" : ["A.html", "B.html", "C.html"],
                     "2" : ["C.html","D.html","E.html"]
                     }
    
    def get(self):
        try:
            utm = self.get_argument("utm_id")
            expectedConv = 100 / len(Server.web_page_dict[utm])
            for page in Server.web_page_dict[utm]:
                if(Tracker.getScore(utm, page) <= expectedConv): 
                    self.write(open(page).read())
                    return;
        except Exception as exc:
            self.write({"error": str(exc)})
            

ROUTES = [
    (r"/", Server),
    (r"/track", TrackingHandler),
    (r"/summaryJson", AjaxSummaryJsonHandler),
    (r"/static/(.*)",web.StaticFileHandler,{'path':'./static/'}),
    (r"/summary()",web.StaticFileHandler,{'path':'./summary.html'})
    
]


def run():
    app = web.Application(
        ROUTES,
        debug=True,
    )

    app.listen(8000)
    print("Server (re)started. Listening on port " + str(8000))

    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    run()
