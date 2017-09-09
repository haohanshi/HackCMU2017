from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
import cgi
import json
from distutils.util import strtobool
from main import *


class Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        rootdir = '/Users/Alex/Desktop/HackCMU217' #file location
        try:
            self.send_response(200)
            self.send_header('Content-type',    'text/html')
            self.end_headers()
            if self.path.endswith('.html'):
                print(rootdir + self.path)
                f = open(rootdir + self.path)
                #send file content to client
                self.wfile.write(f.read())
                f.close()
        except IOError:
            self.send_error(404, 'file not found')
        return

    def parser(self,room):
        if room == "Randy+Pausch+Bridge":
            building = "RPB"
            number = 5000
            type = 'Road'
            level = 5
            name = "Randy Pausch Bridge"
        else:
            building,number=room.split("+")
            name=building+number
            type='Room'
            level=number[0]
            if level=='A':
                level=0
            else:
                level = int(level)
            number = int(number)
        return [name,type,building,level,number]


    def do_POST(self):
        arg_dict = dict()
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        # Begin the response
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # Echo back information about what was posted in the form
        for field in form.keys():
            field_item = form[field]
            # Regular form value
            arg_dict[field] = form[field].value
            # self.wfile.write('\t%s=%s\n' % (field, form[field].value))
        start_room = arg_dict["Start"]
        end_room = arg_dict["End"]
        elevator = arg_dict["elevator"]
        elevator = bool(strtobool(elevator))
        outdoor = arg_dict["outdoor"]
        outdoor = bool(strtobool(outdoor))
        handicap = arg_dict["handicap"]
        handicap = bool(strtobool(handicap))
        #output start/end locations in list format
        startpoint=self.parser(start_room)
        endpoint=self.parser(end_room)

        dict_t = main(startpoint, endpoint)
        # dict_t = {'description':[
        #     'Walk down the Corridor.You will see DH_2F_WestStair.',
        #     'Climb up the stairs. You will see DH2210.','3','4','5'],'points':['DH_2350_Corridor','DH_2F_WestStair', '3']}
        result = json.dumps(dict_t)
        self.wfile.write(result)
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('128.237.185.123', 8080), Handler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
