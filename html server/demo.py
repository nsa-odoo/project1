from SimpleHTTPServer import SimpleHTTPRequestHandler
import psycopg2
#from config import config
import SocketServer
import simplejson
import urlparse
import os
from os import curdir, sep
import mimetypes

class S(SimpleHTTPRequestHandler):

    def connect(self):
        return psycopg2.connect(database="test", user="nirali",host="localhost", password="nirali", port="5432")

    def do_GET(self):
        mime = {"html":"text/html", "css":"text/css", "png":"image/png"}
        a = ""
        if a in mime.keys():
            self.send_response(200)
            self.send_header('Content-type', mime[a])
            self.end_headers()
            print a
            f = open(curdir + sep + self.path)             
            self.wfile.write(f.read())              
            f.close()
        return SimpleHTTPRequestHandler.do_GET(self)
        
    def do_POST(self):
        print "got post!!"
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        dict=urlparse.parse_qs(post_body)
        print dict
        username = dict["username"][0]
        password =  dict["password"][0]
        self.insert_record(username,password)
        return self.wfile.write('<h1>Success!</h1>')

    def insert_record(self,UserName,PassWord):
        conn = self.connect()
        cur = conn.cursor()
        query = "insert into data(username,password) values(%s,%s);"
        data = (UserName,PassWord)
        cur.execute(query,data)
        conn.commit()
        conn.close()


def run(handler_class=S, port=80):
    httpd = SocketServer.TCPServer(("", port), handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
