from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
import cgi
import json
import main.py


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
        building,number=room.split(" ")
        name=building+number
        type='Room'
        level=int(number[0])
        number = int(number)
        if level=='A':
            level=0
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
        self.end_headers()

        # Echo back information about what was posted in the form
        for field in form.keys():
            field_item = form[field]
            # Regular form value
            arg_dict[field] = form[field].value
            # self.wfile.write('\t%s=%s\n' % (field, form[field].value))
        print arg_dict
        start_room = arg_dict["Start"]
        end_room = arg_dict["End"]
        #output start/end locations in list format
        startpoint=self.parser(start_room)
        endpoint=self.parser(end_room)
        dict_t = main(startpoint, endpoint)
        result = json.dumps(arg_dict)
        self.wfile.write(result)
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8080), Handler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
