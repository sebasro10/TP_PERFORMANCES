import grpc
from concurrent import futures
import movie_pb2
import movie_pb2_grpc
import json

class MovieServicer(movie_pb2_grpc.MovieServicer):

    def __init__(self):
        with open('{}/database/movies.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["movies"]

    def Home(self, request, context):
        return movie_pb2.Message(message="<h1 style='color:blue'>Welcome to the Movie service!</h1>")

    def GetListMovies(self, request, context):
        return movie_pb2.MovieDataArray(movies=self.db)
    
    def GetMovieByID(self, request, context):
        for movie in self.db:
            if movie['id'] == request.id:
                return movie_pb2.MovieData(id=movie["id"],rank=movie["rank"],title=movie["title"],fullTitle=movie["fullTitle"],year=movie["year"],image=movie["image"],imDbRating=movie["imDbRating"],imDbRatingCount=movie["imDbRatingCount"],director=movie["director"])
        return movie_pb2.MovieData(id="",rank="",title="",fullTitle="",year="",image="",imDbRating="",imDbRatingCount="")
    
    def CreateMovie(self, request, context):
        for movie in self.db:
            if movie['id'] == request.id:
                return movie_pb2.Message(message="movie ID already exists")
        self.db.append({'id':request.id,'rank':request.rank,'year':request.year,'image':request.image,'title':request.title,'fullTitle':request.fullTitle,'imDbRating':request.imDbRating,'imDbRatingCount':request.imDbRatingCount,'director':request.director})
        return movie_pb2.Message(message="movie added")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    movie_pb2_grpc.add_MovieServicer_to_server(MovieServicer(), server)
    server.add_insecure_port('[::]:5002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
