from flask import render_template, request, redirect, url_for


def init_app(app):
    players = ['apEX', 'ropz', 'Zywoo', 'flameZ', 'mezii']
    players2 = ['chopper', 'sh1ro', 'zont1x', 'donk', 'zweih']
    players3 = ['bLitz', 'Techno', 'Senzu', 'mzinho', '910']
    players4 = ['Brollan', 'torzsi', 'Spinx', 'Jimpphat', 'xertioN']
    players5 = ['MAJ3R', 'XANTARES', 'woxic', 'Wicadia', 'jottAAA']
    

    @app.route('/')
    def home(): 
        return render_template('index.html')

    @app.route('/teams', methods=['GET', 'POST'])
    def teams():
        teams = ['Vitality', 'Spirit', 'The MongolZ', 'MOUZ', 'Aurora']


        if request.method == 'POST':
            if request.form.get('player'):
                players.append(request.form.get('player'))
                return redirect(url_for('teams'))

        return render_template('teams.html', players=players, players2= players2, players3=players3, players4=players4, players5=players5, teams=teams)

    @app.route('/newplayer', methods=['GET', 'POST'])
    def newplayer():

        if request.method == 'POST':
            if request.form.get('name') and request.form.get('team') and request.form.get('title'):
                return redirect(url_for('newplayer'))
        return render_template('newPlayer.html')
