import random
import string


def get_random_string(length):
    # Create random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str


def generate_api(questionnaire_data):
    youtube_weights = {}
    book_weights = {}
    movie_genre_weights = {}
    movie_min_imdb = 0
    movie_language_weights = {}
    spotify_genre_weights = {}
    spotify_artist_weights = {}
    spotify_track_weights = {}

    for user_data in questionnaire_data:
        # youtube
        if "youtube" in user_data:
            youtube = user_data["youtube"]
            current_weight = 5
            for i in range(len(youtube)):
                if youtube[i] in youtube_weights:
                    youtube_weights[youtube[i]] += current_weight
                else:
                    youtube_weights[youtube[i]] = current_weight

                current_weight -= 1

        # book
        if "book" in user_data:
            book = user_data["book"]
            current_weight = 5
            for i in range(len(book)):
                if book[i] in book_weights:
                    book_weights[book[i]] += current_weight
                else:
                    book_weights[book[i]] = current_weight

                current_weight -= 1

        # movie
        if "movie" in user_data:
            movie = user_data["movie"]

            # movie - genre
            genre = movie["genre"]
            current_weight = 5
            for i in range(len(genre)):
                if genre[i] in movie_genre_weights:
                    movie_genre_weights[genre[i]] += current_weight
                else:
                    movie_genre_weights[genre[i]] = current_weight

                current_weight -= 1

            # movie - imdb
            movie_min_imdb = max(movie_min_imdb, movie["imdb"])

            # movie - language
            language = movie["language"]
            current_weight = 5
            for i in range(len(language)):
                if language[i] in movie_language_weights:
                    movie_language_weights[language[i]] += current_weight
                else:
                    movie_language_weights[language[i]] = current_weight

                current_weight -= 1

        # spotify
        if "spotify" in user_data:
            spotify = user_data["spotify"]

            # spotify - genre
            genre = spotify["genre"]
            current_weight = 5
            for i in range(len(genre)):
                if genre[i] in spotify_genre_weights:
                    spotify_genre_weights[genre[i]] += current_weight
                else:
                    spotify_genre_weights[genre[i]] = current_weight

                current_weight -= 1

            # spotify - artist
            artist = spotify["artist"]
            current_weight = 5
            for i in range(len(artist)):
                if artist[i] in spotify_artist_weights:
                    spotify_artist_weights[artist[i]] += current_weight
                else:
                    spotify_artist_weights[artist[i]] = current_weight

                current_weight -= 1

            # spotify - track
            track = spotify["track"]
            current_weight = 5
            for i in range(len(track)):
                if track[i] in spotify_track_weights:
                    spotify_track_weights[track[i]] += current_weight
                else:
                    spotify_track_weights[track[i]] = current_weight

                current_weight -= 1

    # sort dictionary
    youtube_weights = {k: v for k, v in sorted(
        youtube_weights.items(), key=lambda item: item[1], reverse=True)}
    book_weights = {k: v for k, v in sorted(
        book_weights.items(), key=lambda item: item[1], reverse=True)}
    movie_genre_weights = {k: v for k, v in sorted(
        movie_genre_weights.items(), key=lambda item: item[1], reverse=True)}
    movie_language_weights = {k: v for k, v in sorted(
        movie_language_weights.items(), key=lambda item: item[1], reverse=True)}
    spotify_genre_weights = {k: v for k, v in sorted(
        spotify_genre_weights.items(), key=lambda item: item[1], reverse=True)}
    spotify_artist_weights = {k: v for k, v in sorted(
        spotify_artist_weights.items(), key=lambda item: item[1], reverse=True)}
    spotify_track_weights = {k: v for k, v in sorted(
        spotify_track_weights.items(), key=lambda item: item[1], reverse=True)}

    # number of items to return
    no_youtube = min(len(youtube_weights), 3)
    no_movie_genre = min(len(movie_genre_weights), 3)
    no_movie_language = min(len(movie_language_weights), 3)
    no_spotify_genre = min(len(spotify_genre_weights), 3)
    no_spotify_artist = min(len(spotify_artist_weights), 3)
    no_spotify_track = min(len(spotify_track_weights), 3)

    youtube_categories = {'1': 'Film & Animation', '2': 'Autos & Vehicles', '10': 'Music', '15': 'Pets & Animals', '17': 'Sports', '19': 'Travel & Events', '20': 'Gaming',
                          '22': 'People & Blogs', '23': 'Comedy', '24': 'Entertainment', '25': 'News & Politics', '26': 'Howto & Style', '27': 'Education', '28': 'Science & Technology'}

    api_param = {}
    youtube_encoded = list(youtube_weights.keys())[0:no_youtube]
    youtube_decoded = []
    for item in youtube_encoded:
        youtube_decoded.append(youtube_categories[item])

    api_param["youtube"] = {"videoCategory": list(youtube_weights.keys())[
        0], "videoMore": ",".join(youtube_decoded)}
    api_param["book"] = {"subject": list(book_weights.keys())[0]}
    api_param["movie"] = {"genre": ",".join(list(movie_genre_weights.keys())[0:no_movie_genre]), "language": ",".join(
        list(movie_language_weights.keys())[0:no_movie_language]), "min_imdb": movie_min_imdb}
    api_param["spotify"] = {"seed_genres": ",".join(list(spotify_genre_weights.keys())[0:no_spotify_genre]), "seed_artists": ",".join(list(
        spotify_artist_weights.keys())[0:no_spotify_artist]), "seed_tracks": ",".join(list(spotify_track_weights.keys())[0:no_spotify_track])}

    return api_param
