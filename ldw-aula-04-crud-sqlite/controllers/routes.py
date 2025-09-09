from flask import render_template, request, redirect, url_for
import urllib  # Envia requisições a uma URL
import json  # Converte os dados em JSON -> dicionário
from models.database import Game, db # Importando o model de Game


def init_app(app):
    # Lista em Python(array)
    players = ['Yan', 'Ferrari', 'Valéria', 'Amanda']
    gamelist = [{'Título': 'CS 1.6', 'Ano': 1996, 'Categoria': 'FPS Online'}]

    @app.route('/')
    def home():  # Função que será executada ao acessar a rota
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        title = 'Tarisland'
        year = 2022
        category = 'MMORPG'
        # Dicionário em Python (objeto)
        console = {'Nome': 'Playstation 5', 'Fabricante': 'Sony', 'Ano': 2020}

        # Tratando uma requisição POST com request

        if request.method == 'POST':
            # Coletando o texto da INPUT
            if request.form.get('player'):
                players.append(request.form.get('player'))
                return redirect(url_for('games'))

        return render_template('games.html', title=title, year=year, category=category, players=players, console=console)

    @app.route('/newGame', methods=['GET', 'POST'])
    def newgame():

        # Tratando requisição a POST
        if request.method == 'POST':
            if request.form.get('title') and request.form.get('year') and request.form.get('category'):
                gamelist.append({'Título': request.form.get('title'), 'Ano': request.form.get(
                    'year'), 'Categoria': request.form.get('category')})
                return redirect(url_for('newgame'))
        return render_template('newGame.html', gamelist=gamelist)

    @app.route('/apigames', methods=['GET', 'POST'])
    # Criando parâmetros para rota
    @app.route('/apigames/<int:id>', methods=['GET', 'POST'])
    def apigames(id=None):  # Parâmetro opcional
        url = 'https://www.freetogame.com/api/games'
        response = urllib.request.urlopen(url)
        data = response.read()
        # Pega a informação e transforma em dicionário
        gamesList = json.loads(data)
        # Verificando se o parâmetro foi enviado
        if id:
            gameInfo = []
            for game in gamesList:
                # Comparando os IDs (se o Id da URL bate com o Id da Lista)
                if game['id'] == id:
                    gameInfo = game
                    break
            if gameInfo: 
                return render_template('gameinfo.html', gameInfo=gameInfo)
            else:
                return f'Game com o ID {id} não foi encontrado'
        else:
            return render_template('apigames.html', gamesList=gamesList)
        
    @app.route('/estoque', methods=["GET", "POST"])
    @app.route('/estoque/delete/<int:id>')
    def estoque(id=None):

        # Se o ID for enviado
        if id:
            # Selecionando o jogo pelo ID
            game = Game.query.get(id)
            # Deleta o jogo pelo ID
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque'))

        if request.method == 'POST':
            
            # Realiza o cadastro do jogo
            newGame = Game(request.form['title'], request.form['year'], request.form['category'], request.form['platform'], request.form['price'], request.form['quantity'])
            
            # .session.add é um método do SQLAlchemy para gravar registros no banco
            db.session.add(newGame)
            # .session.commit confirma as alterações do banco
            db.session.commit()
            return redirect(url_for('estoque'))

        # query.all é o método do SQL Alchemy para selecionar todos os registros
        gamesEstoque = Game.query.all()
        return render_template('estoque.html', gamesEstoque=gamesEstoque)
    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit(id):
        game = Game.query.get(id)

        if request.method == 'POST':
            game.title = request.form['title']
            game.year = request.form['year']
            game.category = request.form['category']
            game.platform = request.form['platform']
            game.price = request.form['price']
            game.quantity = request.form['quantity']
            db.session.commit()
            return redirect(url_for('estoque'))

        return render_template('editgame.html', game=game)