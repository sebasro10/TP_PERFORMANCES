import json

def home(_,info):
    return {"message":"<h1 style='color:blue'>Welcome to the Movie service!</h1>"}

def get_list_movies(_,info):
    with open('{}/database/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        return movies['movies']

def movie_with_id(_,info,_id):
    with open('{}/database/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie

def create_movie(_,info,_movie):
    with open('{}/database/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)
        for movie in movies['movies']:
            if movie['id'] == _movie["id"]:
                return {"message":"movie ID already exists"}
    movies['movies'].append(_movie)
    with open('{}/database/movies.json'.format("."), "w") as wfile:
        json.dump(movies, wfile)
    return {"message":"movie added"}
