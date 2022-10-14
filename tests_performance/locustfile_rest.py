from locust import HttpUser, task

class Rest(HttpUser): 
    
    @task 
    def home(self): 
        self.client.get(url='/')

    @task 
    def get_movies(self): 
        self.client.get(url='/movies')
    
    @task 
    def get_movie_byid(self): 
        self.client.get(url='/movies/tt3315342')
    
    @task 
    def route(self): 
        self.client.post(url='/movies/newId', json={
            "id": "newId",
            "rank": "400",
            "title": "New title",
            "fullTitle": "New title (1994)",
            "year": "1994",
            "image": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_Ratio0.6716_AL_.jpg",
            "imDbRating": "9.2",
            "imDbRatingCount": "2649185",
            "director": {
                "firstName": "New",
                "lastName": "Director"
            }
        })
