from flask import render_template, request, redirect, url_for


def init_app(app):
    warriors = ['Stephen Curry', 'Brandin Podziemski', 'Jimmy Butler III', 'Draymond Green', 'Quinten Post']
    lakers = ['Luka Dončić', 'Austin Reaves', 'Rui Hachimura', 'Lebron James', 'Deandre Ayton']
    celtics = ['Payton Pritchard','Anfernee Simons', 'Derrick White', 'Jaylen Brown', 'Al Horford']
    spurs = ["De'Aaron Fox", 'Stephon Castle', 'Devin Vassell', 'Harrison Barnes', 'Victor Wembanyama']
    bulls = ['Josh Giddey', 'Coby White', 'Kevin Huerter', 'Patrick Williams', 'Nikola Vučević']
    teamlist = [{'Nome': 'Warriors', 'Divisão': 'Oeste', 'Títulos': 6}]

    @app.route('/')
    def home(): 
        return render_template('index.html')

    @app.route('/teams', methods=['GET', 'POST'])
    def teams():
        teams = ['Golden State Warriors', 'Los Angeles Lakers', 'Boston Celtics', 'San Antonio Spurs', 'Chicago Bulls']

        if request.method == 'POST':
            if request.form.get('player'):
                warriors.append(request.form.get('player'))
                return redirect(url_for('teams'))

        return render_template('teams.html', warriors=warriors, lakers=lakers, celtics=celtics, spurs=spurs, bulls=bulls, teams=teams)

    @app.route('/newTeam', methods=['GET', 'POST'])
    def newteam():

        if request.method == 'POST':
            if request.form.get('name') and request.form.get('division') and request.form.get('title'):
                teamlist.append({'Nome': request.form.get('name'), 'Divisão': request.form.get('division'), 'Títulos': request.form.get('title')})
                return redirect(url_for('newteam'))
        return render_template('newTeam.html', teamlist=teamlist)