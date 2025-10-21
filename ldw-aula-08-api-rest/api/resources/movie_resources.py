# Importando a class Resource do Flask Restful
from flask_restful import Resource

# Importando a variável api do pacote api
from api import api 

# Importando pacotes do Flask
from flask import make_response, jsonify

# Importando os schemas
from ..schemas import movie_schema

# Importando o Model
from ..models import movie_model

# Importando o Service
from ..services import movie_service

# Criando os recursos de filmes
class MoviesList(Resource):
    # Método GET: Listar
    def get(self):
        movies = movie_service.get_movies()
        movieSchema = movie_schema.MovieSchema(many=True)
        return make_response(movieSchema.jsonify(movies), 200)
    
class RecursosAPI(Resource):
    def get(self):
        return "Você enviou uma requisição GET!"
    
    def post(self):
        return "Você enviou uma requisição POST!"
    
    def put(self):
        return "Você enviou uma requisição PUT!"
    
    def delete(self):
        return "Você enviou uma requisição DELETE!"
api.add_resource(MoviesList, '/movies')
api.add_resource(RecursosAPI, '/recursos')