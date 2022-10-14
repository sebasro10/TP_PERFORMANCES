from locust import HttpUser, task

class Rest2(HttpUser): 
    
    @task 
    def get_movies(self): 
        self.client.get(url='/movies')

    @task 
    def get_movie_byid(self): 
        self.client.get(url='/movies/tt3315342')
