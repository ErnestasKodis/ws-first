from curses.ascii import DEL
from flask import Flask, Response, request, jsonify, abort
import json
import random
application = Flask(__name__)

current_id = 5

@application.route('/')
def init():
    return 'Hello'

movies = [
    {"id" : 1,
    "title" : "Uncharted",
    "director" : "Ruben Fleischer",
    "rating" : 6.6,
    "release_year" : 2022
    },
    {"id" : 2,
    "title" : "Fight Club",
    "director" : "David Fincher",
    "rating" : 8.8,
    "release_year" :1999
    },
    {"id" : 3,
    "title" : "The Godfather",
    "director" : "Francis Ford Coppola",
    "rating" : 9.2,
    "release_year" : 1972
    },
    {"id" : 4,
    "title" : "The Dark Knight",
    "director" : "Christopher Nolan",
    "rating" : 9.0,
    "release_year" : 2008
    }]

@application.route('/api/movies', methods = ["GET"])  # Returns full movie list
def movieList():
    return jsonify (movies)

@application.route('/api/movies/<int:movieId>', methods = ["GET"])
def get_movie_byID(movieId):
    for movie in movies:
        if movie["id"] == movieId:
            return jsonify(movie)
    error = "Movie with ID: " + str(movieId) + " wasn't found"
    return Response(json.dumps({"Failure": error}), status=404, mimetype="application/json")

@application.route('/api/movies', methods = ["POST"])
def add_movie():
    new_movie_data = request.get_json()
    if "title" in new_movie_data and "director" in new_movie_data and "rating" in new_movie_data and "release_year" in new_movie_data:
        global current_id
        new_movie ={
            "id" : current_id,
            "title" : new_movie_data["title"],
            "director" : new_movie_data["director"],
            "rating" : new_movie_data["rating"],
            "release_year" : new_movie_data["release_year"]
        }
        movies.append(new_movie)
        current_id += 1
        return Response((json.dumps({"Success":"Movies was added to the list;" + str(jsonify(new_movie))})), status = 201, headers={"location": "/api/movies/"+str(new_movie["id"]-1 )}, mimetype="application/json")
    else:
        error = "Missing "
        if "title" not in new_movie_data:
            error += "title; "
        if "director" not in new_movie_data:
            error += "director; "
        if "rating" not in new_movie_data:
            error += "rating; "
        if "release_year" not in new_movie_data:
            error += "release year; "
        return Response(json.dumps({"Failure" : error}, status=400, mimetype="application/json"))

@application.route("/api/movies/<int:movieId>", methods = ["PATCH"])
def put_movie(movieId):
    movieId -= 1
    new_movie_data = request.get_json()
    if "title" not in new_movie_data and "director" not in new_movie_data and "rating" not in new_movie_data and "release_year" not in new_movie_data:
        error = "Missing "
        if "title" not in new_movie_data:
            error += "title; "
        if "director" not in new_movie_data:
            error += "director; "
        if "rating" not in new_movie_data:
            error += "rating; "
        if "release_year" not in new_movie_data:
            error += "release year; "
        error += ". Please specify Body"
        return Response(json.dumps({"Failure" : error}),status=404, mimetype="application/json")
    message = ""
    if "title" in new_movie_data:
        movies[movieId]["title"] = new_movie_data["title"]
        message += "Model; "
    if "director" in new_movie_data:
        movies[movieId]["director"] = new_movie_data["director"]
        message += "Director; "
    if "rating" in new_movie_data:
        movies[movieId]["rating"] = new_movie_data["rating"]
        message  += "Rating; "
    if "release_year" in new_movie_data:
        movies[movieId]["release_year"] = new_movie_data["release_year"]
        message += "Release year; "
    message += "have been changed"
    return Response(json.dumps(movies[movieId]), status=200, mimetype="application/json")

@application.route("/api/movies/<int:movieId>", methods = ["DELETE"])
def delete_movie(movieId):
    for movie in movies:
        if movie["id"] == movieId:
            movies.remove(movie)
            return Response(response=(json.dumps({"Success" : "Deleted"})), status=204, mimetype="application/json")
    error = "Movie with ID: " + str(movieId) + " wasn't found"
    return Response(json.dumps({"Failure": error}), status=400, mimetype="application/json")


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
