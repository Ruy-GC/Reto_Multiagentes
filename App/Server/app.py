from flask import Flask, request,json
from flask_json import FlaskJSON, json_response, as_json

app = Flask(__name__)
JSON = FlaskJSON(app)

@app.route("/agentpy_json", methods = ['GET'])
@as_json
def agentpy_get_data():
    agents = json.load(open('./data.json'))
    return json_response(data = agents )
    


@app.route("/agentpy_json", methods = ['POST'])
def agentpy_send_data():

    data = request.get_json(force=True)

    with open('./data.json', 'w') as outfile:
        outfile.write(json.dumps(data, indent = 4))
    
    outfile.close()

    return "Data Loaded correctly from agentpy"

if __name__ == '__main__':
    app.run()

