'''
Created on Feb 10, 2017
@author: anujjain
'''

from random import randint
from tornado import ioloop, web

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
            utm_id = self.get_argument("utm_id")
            self.write(open(Server.web_page_dict[utm_id][randint(0,len(Server.web_page_dict[utm_id])-1)]).read())
        except Exception as exc:
            self.write({"error": str(exc)})
            

ROUTES = [
    (r"/", Server)        
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
