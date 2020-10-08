from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/questionnaire' # ENTER DB NAME HERE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

# Stores questionnaire data (should create other tables as there are arrays?)
class Questionnaire(db.Model):
    __tablename__ = 'questionnaire'

    # add in movie_language, min IMDB rating.
    user_id = db.Column(db.Integer, primary_key=True)
    youtube_category = db.Column(db.String(64))
    movie_genre = db.Column(db.String(64))
    book_subject = db.Column(db.String(64))
    artist = db.Column(db.String(64))
    track = db.Column(db.String(64))
    music_genre = db.Column(db.String(64))

    def __init__(self, youtube_category, movie_genre, book_subject, artist, track, music_genre):
        self.user_id = user_id

        self.youtube_category = youtube_category
        self.movie_genre = movie_genre
        self.book_subject = book_subject
        self.artist = artist
        self.track = track
        self.music_genre = music_genre


    def json(self):
        data = {
            "youtube_category": [self.youtube_category],
            "movie_genre": [self.movie_genre],
            "book_subject": [self.book_subject],
            "artist": [self.artist],
            "track": [self.track],
            "music_genre": [self.music_genre]
        }
        return data

# test
@app.route("/")
def test():
    return "working!"

# accepting questionnaire data
@app.route("/questionnaire/", methods=['POST'])
def questionnaireData():
    data = request.get_json()
    print(data)

    try:
        db.session.add(**data)
        db.session.commit()  # keep getting error, probably because of the arrays.
    except:
        return jsonify({"message": "An error occurred creating the record."}), 500
    
    return jsonify(data), 201

# To continue: getting required parameters for APIs (query after questionnaire data can be stored)


if __name__ == "__main__":
	app.run(port=5001, debug=True)