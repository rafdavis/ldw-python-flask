from flask import render_template, request, redirect, url_for
from models.database import db, Nba
import urllib
import json


def init_app(app):
    warriors = ['Stephen Curry', 'Brandin Podziemski',
                'Jimmy Butler III', 'Draymond Green', 'Quinten Post']
    lakers = ['Luka Dončić', 'Austin Reaves',
              'Rui Hachimura', 'Lebron James', 'Deandre Ayton']
    celtics = ['Payton Pritchard', 'Anfernee Simons',
               'Derrick White', 'Jaylen Brown', 'Al Horford']
    spurs = ["De'Aaron Fox", 'Stephon Castle', 'Devin Vassell',
             'Harrison Barnes', 'Victor Wembanyama']
    bulls = ['Josh Giddey', 'Coby White', 'Kevin Huerter',
             'Patrick Williams', 'Nikola Vučević']
    teamlist = [{'Nome': 'Warriors', 'Divisão': 'Oeste', 'Títulos': 6}]

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/teams', methods=['GET', 'POST'])
    def teams():
        teams = ['Golden State Warriors', 'Los Angeles Lakers',
                 'Boston Celtics', 'San Antonio Spurs', 'Chicago Bulls']

        if request.method == 'POST':
            if request.form.get('player'):
                warriors.append(request.form.get('player'))
                return redirect(url_for('teams'))
        return render_template('teams.html', warriors=warriors, lakers=lakers, celtics=celtics, spurs=spurs, bulls=bulls, teams=teams)

    @app.route('/newTeam', methods=['GET', 'POST'])
    @app.route('/newTeam/delete/<int:id>')
    def newteam(id=None):
        if id:
            team = Nba.query.get(id)
            db.session.delete(team)
            db.session.commit()
            return redirect(url_for('newteam'))

        if request.method == 'POST':
            newTeam = Nba(
                time=request.form['time'],
                divisao=request.form['divisao'],
                titulos=request.form['titulos'],
                estadio=request.form['estadio']
            )
            db.session.add(newTeam)
            db.session.commit()
            return redirect(url_for('newteam'))
        else:

            page = request.args.get('page', 1, type=int)

            per_page = 3

            teams_page = Nba.query.paginate(page=page, per_page=per_page)
            return render_template('newTeam.html', times=teams_page)

    @app.route('/apinba', methods=['GET', 'POST'])
    @app.route('/apinba/<idTeam>', methods=['GET', 'POST'])
    def apinba(idTeam=None):
        url = 'https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l=NBA'
        response = urllib.request.urlopen(url)
        data = response.read()
        teamList = json.loads(data)
        teams = teamList["teams"]

        if idTeam:
            teaminfo = None
            for team in teamList["teams"]:
                if team['idTeam'] == idTeam:
                    teaminfo = team
                    break
            if teaminfo:
                return render_template('teamInfo.html', teaminfo=teaminfo)
            else:
                return f'Time com a ID {idTeam} não foi encontrado'
        else:
            return render_template('apinba.html', teamList=teams)

    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit(id):
        team = Nba.query.get(id)
        return render_template('editTeam.html', team=team)