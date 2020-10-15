from flask import Flask, request, jsonify
from flask_cors import CORS
from firebase_admin import credentials, firestore, initialize_app

import json
import utility


app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
room_ref = db.collection('rooms')


@app.route('/create-room/<string:room_name>', methods=['GET'])
def create(room_name):
    random_code = utility.get_random_string(6)

    # checks if random_code already exists
    room = room_ref.document(random_code).get()
    while (room.to_dict() != None):
        random_code = utility.get_random_string(6)
        room = room_ref.document(random_code).get()

    try:
        obj = {"room_name": room_name, "questionnaire": []}
        room_ref.document(random_code).set(obj)
        return jsonify({"room_code": random_code, "room_name": room_name}), 200
    except Exception as e:
        return f"{e}", 400


@app.route('/room/<string:room_code>', methods=['GET'])
def get_room(room_code):
    """
        read() : Fetches documents from Firestore collection as JSON.
        todo : Return document that matches query ID.
        all_todos : Return all documents.
    """
    try:
        room = room_ref.document(room_code).get()
        if room.to_dict() == None:  # room code doesn't exist
            return "Invalid room code", 400
        return jsonify(room.to_dict()), 200
    except Exception as e:
        return f"{e}", 400


@app.route('/add-questionnaire/<string:room_code>', methods=['POST'])
def add_questionnaire(room_code):

    try:
        questionnaire_data = request.get_json()

        room = room_ref.document(room_code).get()
        room = room.to_dict()
        room["questionnaire"].append(questionnaire_data)

        room_ref.document(room_code).set(room)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"{e}", 400


@app.route('/recommend/<string:room_code>', methods=['GET'])
def update(room_code):

    try:
        questionnaire_data = request.get_json()

        room = room_ref.document(room_code).get()
        room = room.to_dict()

        if (len(room["questionnaire"]) == 0):
            return "At least one user needs to complete the questionnaire", 400

        return jsonify(utility.generate_api(room["questionnaire"])), 200
    except Exception as e:
        return f"{e}", 400


# This is for flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
