from locust import HttpUser, task, tag

class GraphQL2(HttpUser):
    
    @task 
    def get_movie_titles(self): 
        self.client.post(url='/graphql', json={'query': 
            """query{get_list_movies{
                title
            } }"""}, name="get_movie_titles")
    
    @task 
    def get_movie_title_byid(self): 
        self.client.post(url='/graphql', json={'query': 
            """query{movie_with_id(_id:"tt3315342"){
                title
            } }"""}, name="get_movie_title_byid")
