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
    return render_template('games.html')

# Se for o arquivo for executado diretamente pelo interpretador o servidor é iniciado
if __name__ == '__main__':

    # Iniciando o servidor
    app.run(host='localhost', port=5000, debug=True) 

# python arquivo.py (PARA EXECUTAR)