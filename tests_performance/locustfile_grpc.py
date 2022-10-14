import grpc
import movie_pb2_grpc
import movie_pb2
from locust import User, task
from locust.exception import LocustError
from google.protobuf.json_format import MessageToJson
import time

class GrpcClient:
    def __init__(self, environment, stub):
        self.env = environment
        self._stub_class = stub.__class__
        self._stub = stub

    def __getattr__(self, name):
        func = self._stub_class.__getattribute__(self._stub, name)

        def wrapper(*args, **kwargs):
            request_meta = {
                "request_type": "grpc",
                "name": name,
                "start_time": time.time(),
                "response_length": 0,
                "exception": None,
                "context": None,
                "response": None,
            }
            start_perf_counter = time.perf_counter()
            try:
                request_meta["response"] = func(*args, **kwargs)
                request_meta["response_length"] = len(MessageToJson(request_meta["response"]))
            except grpc.RpcError as e:
                request_meta["exception"] = e
            request_meta["response_time"] = (time.perf_counter() - start_perf_counter) * 1000
            self.env.events.request.fire(**request_meta)
            return request_meta["response"]

        return wrapper


class GrpcUser(User):
    abstract = True

    stub_class = None

    def __init__(self, environment):
        super().__init__(environment)
        for attr_value, attr_name in ((self.host, "host"), (self.stub_class, "stub_class")):
            if attr_value is None:
                raise LocustError(f"You must specify the {attr_name}.")
        self._channel = grpc.insecure_channel(self.host)
        self._channel_closed = False
        stub = self.stub_class(self._channel)
        self.client = GrpcClient(environment, stub)


class Grpc(GrpcUser):
    host = "localhost:5002"
    stub_class = movie_pb2_grpc.MovieStub

    @task
    def Home(self):
        if not self._channel_closed:
            self.client.Home(movie_pb2.Empty())
        time.sleep(1)
    
    @task
    def GetListMovies(self):
        if not self._channel_closed:
            self.client.GetListMovies(movie_pb2.Empty())
        time.sleep(1)
    
    @task
    def GetMovieByID(self):
        if not self._channel_closed:
            self.client.GetMovieByID(movie_pb2.MovieID(id="tt3315342"))
        time.sleep(1)

    @task
    def CreateMovie(self):
        if not self._channel_closed:
            self.client.CreateMovie(movie_pb2.MovieData(id="newId",rank="400",title="New title",fullTitle="New title (1994)",year="1994",image="https=//m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_Ratio0.6716_AL_.jpg",imDbRating="9.2",imDbRatingCount="2649185",director={"firstName":"New","lastName":"Director"}))
        time.sleep(1)
