from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import json

app = Flask(__name__)
dbURL = 'mysql+mysqlconnector://admin:Commonette234!@commonette.ciygr11ayijs.ap-southeast-1.rds.amazonaws.com:3306/commonette'
app.config['SQLALCHEMY_DATABASE_URI'] = dbURL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

# Stores questionnaire data (should create other tables as there are arrays?)
class Questionnaire(db.Model):
    __tablename__ = 'questionnaire'

    # add in movie_language, min IMDB rating.
    user_id = db.Column(db.Integer, primary_key=True)
    youtube_category_stored_id = db.Column(db.Integer)
    # youtube_category = db.Column(db.String(64))
    # movie_genre = db.Column(db.String(64))
    # book_subject = db.Column(db.String(64))
    # artist = db.Column(db.String(64))
    # track = db.Column(db.String(64))
    # music_genre = db.Column(db.String(64))

    # def __init__(self, youtube_category, movie_genre, book_subject, artist, track, music_genre):
    #     self.user_id = user_id

    #     self.youtube_category = youtube_category
    #     self.movie_genre = movie_genre
    #     self.book_subject = book_subject
    #     self.artist = artist
    #     self.track = track
    #     self.music_genre = music_genre

    def __init__(self, user_id, youtube_category_stored_id):
        self.user_id = user_id
        self.youtube_category_stored_id = youtube_category_stored_id

    def json(self):
        data = {
            "youtube_category_id": self.youtube_category_id
            # "movie_genre": self.movie_genre,
            # "book_subject": self.book_subject,
            # "artist": self.artist,
            # "track": self.track,
            # "music_genre": self.music_genre
        }
        return data
    
class Q_youtube(db.Model):
    __table_name__ = "q_youtube"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    youtube_category_stored_id = db.Column(db.Integer)
    youtube_category = db.Column(db.String)

    def __init__(self, id, user_id, youtube_category_stored_id, youtube_category):
        self.id = id
        self.user_id = user_id
        self.youtube_category_stored_id = youtube_category_stored_id
        self.youtube_category = youtube_category

    def json(self):
        data = {
            "user_id": self.user_id,
            "youtube_category_stored_id": self.youtube_category_stored_id,
            "youtube_category": self.youtube_category
        }
        return data


# test
@app.route("/")
def test():
    return "working!"

# accepting questionnaire data
@app.route("/questionnaire/<int:user_id>/<int:youtube_category_stored_id>", methods=['POST'])
def questionnaireData(user_id, youtube_category_stored_id):
    last_id = Q_youtube.query.order_by(Q_youtube.id.desc()).first()
    if last_id:
        new_id = last_id.id
        new_id += 1
    else:
        new_id = 1

    data = request.get_json()
    # print(type(data))

    for key in data:
        for category in data[key]:
            print(category)
            q_youtube = Q_youtube(new_id, user_id, youtube_category_stored_id, category)

    try:
        db.session.add(q_youtube)
        db.session.commit()  # keep getting error, probably because of the arrays.
    except Exception as e:
        return e
        # return jsonify({"message": "An error occurred creating the record."}), 500
    
    return jsonify(), 201

# To continue: getting required parameters for APIs (query after questionnaire data can be stored)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, threaded=True, debug=True)