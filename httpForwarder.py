import urllib2
from flask import Flask

req = urllib2.Request('http://localhost:8080')
response = urllib2.urlopen(req)
the_page = response.read()

app = Flask(__name__)

@app.route("/")
def hello():
    return the_page

if __name__ == "__main__":
    app.run('0.0.0.0',8081)
