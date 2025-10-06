from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Nba(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.String(150))
    divisao = db.Column(db.String(150))
    titulos = db.Column(db.Integer)
    estadio = db.Column(db.String(150))

    def __init__(self, time, divisao, titulos, estadio):
        self.time = time
        self.divisao = divisao
        self.titulos = titulos
        self.estadio = estadio