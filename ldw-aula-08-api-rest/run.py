from api import app, mongo
# Rodando a aplicação porta 5000 no localhost

# Importando o Model
from api.models.movie_model import Movie

# Importando o Service
from api.services import movie_service

if __name__ == '__main__':
    with app.app_context():
        if 'movies' not in mongo.db.list_collection_names():
            movie = Movie(
                title='',
                description='',
                year=0,
                duration=0
            )
            movie_service.add_movie(movie)

    app.run(debug=True)