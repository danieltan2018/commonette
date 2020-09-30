from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import json
import utility

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:Commonette234!@commonette.ciygr11ayijs.ap-southeast-1.rds.amazonaws.com:3306/commonette'

db = SQLAlchemy(app)
CORS(app)

class Room(db.Model):
    __tablename__ = 'room'
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def json(self):
        dto = {
            'code': self.code, 
            'name': self.name
        }
        return dto  

@app.route("/create-room/<string:room_name>", methods=['GET'])
def create_room(room_name):
    random_code = utility.get_random_string(6)

    # checks if random_code already exists
    while Room.query.filter_by(code=random_code).first():
        random_code = utility.get_random_string(6)
    
    room = Room(code=random_code, name=room_name)
    
    try: 
        db.session.add(room)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating the room."}), 500

    return jsonify(room.json()), 200

# to return api stuff afterwards
@app.route("/room/<string:room_code>", methods=['GET'])
def get_room(room_code):
    room = Room.query.filter_by(code=room_code).first()

    if room:
        return jsonify(room.json()), 200
    else:
        return jsonify({'message': 'Invalid room code'}), 404  

#This is for flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)