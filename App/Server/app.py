from flask import Flask, request,json
from flask_json import FlaskJSON, json_response, as_json
from pyrebase import initialize_app
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
JSON = FlaskJSON(app)

config = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "databaseURL": os.getenv("DATABASE_URL"),
    "storageBucket": os.getenv("STORAGE_BUCKET")
}

firebase = initialize_app(config)
db = firebase.database()

@app.route("/agentpy_json", methods = ['GET'])
@as_json
def agentpy_get_data():
    try:
        data = db.child("data").get()
        print(data.val())
        return json_response(200, res = data.val())
    except:
        return json_response(400, res = "Error while fetching data")



@app.route("/agentpy_json", methods = ['POST'])
@as_json
def agentpy_send_data():

    data = request.get_json(force=True)
    
    try:
        db.child("data").set(data)
        return json_response(200, res = "Data Loaded correctly from agentpy")
    except:
        return json_response(400, res = "Error while loading data")

if __name__ == '__main__':
    app.run()

