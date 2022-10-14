from locust import HttpUser, task, tag

class GraphQL(HttpUser):
    
    @task 
    def home(self): 
        self.client.post(url='/graphql', json={'query': 
            """query{home{
                message
            } }"""}, name="home")

    @task 
    def get_movies(self): 
        self.client.post(url='/graphql', json={'query': 
            """query{get_list_movies{
                id
                rank
                title
                fullTitle
                year
                image
                imDbRating
                imDbRatingCount
                director {
                    firstName
    				lastName
                }
            } }"""}, name="get_movies")
    
    @task 
    def get_movie_byid(self): 
        self.client.post(url='/graphql', json={'query': 
            """query{movie_with_id(_id:"tt3315342"){
                id
                rank
                title
                fullTitle
                year
                image
                imDbRating
                imDbRatingCount
                director {
                    firstName
    				lastName
                }
            } }"""}, name="get_movie_byid")
    
    @task 
    def create_movie(self): 
        self.client.post(url='/graphql', json={'query': 
            """mutation{
                create_movie(_movie:{id:"newId",rank:"400",title:"New title",fullTitle:"New title (1994)",year:"1994",image:"https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_Ratio0.6716_AL_.jpg",imDbRating:"9.2",imDbRatingCount:"2649185",director:{firstName:"New",lastName:"Director"}}) {
                    message
                }
            }"""}, name="create_movie")
