from flask import Flask,jsonify, request

app = Flask(__name__)

data = [
    {
        "id": 1,
        "Name":"Raju",
        "done": False,
        "id": 1
    },
    {
        "Contact": 9347241292,
        "Name":"Rahul",
        "done": False,
        "id":2
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': data[-1]['id'] + 1,
        'title': request.json['title'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    data.append(data)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)