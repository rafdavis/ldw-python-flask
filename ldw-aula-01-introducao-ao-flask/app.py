# Importando o Flask
from flask import Flask, render_template

# Criando uma instância do Flask

app = Flask(__name__, template_folder='views') 
# __name__ Representa o nome da aplicação

# Definindo a rota principal da aplicação '/'


@app.route('/')
def home(): # Função que será executada ao acessar a rota
    return render_template('index.html')

@app.route('/games')
def games():
    title = 'Tarisland'
    year = 2022
    category = 'MMORPG'
    players = ['Yan', 'Ferrari', 'Valéria', 'Amanda']
    # Dicionário em Python (objeto)
    console = {'Nome' : 'Playstation 5', 'Fabricante' : 'Sony', 'Ano' : 2020 }
    return render_template('games.html', title=title, year=year, category=category, players=players, console=console)

# Se for o arquivo for executado diretamente pelo interpretador o servidor é iniciado
if __name__ == '__main__':

    # Iniciando o servidor
    app.run(host='localhost', port=5000, debug=True) 

# python arquivo.py (PARA EXECUTAR)