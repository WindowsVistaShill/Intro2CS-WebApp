#Import libraries
from flask import Flask

#Create application

app = Flask(__name__)

#Create directory
@app.route('/')
def homeA():
    return "My homie @ the homie page put in '\' and then a name if you want"
@app.route('/<name>')
def home(name):
    return "AGGA " + name

#Start application
if __name__ == "__main__":
    app.run()