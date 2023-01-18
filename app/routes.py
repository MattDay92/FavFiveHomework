from app import app
# from folder called app - import the variable app from __init__.py

from flask import render_template

@app.route('/')
def homePage():
    people = ['Shoha', 'Brandt', 'Aubrey']
    artists_list = {'Queen': 'queen.jpeg', 'Foo Fighters': 'foo_fighters.jpeg', 'Stephen Sondheim': 'sondheim.jpeg', 'Joe Iconis':'iconis.jpeg', 'Jonathan Larson': 'larson.jpeg'}
    athletes_list = {'Reggie Miller': 'reggie2.jpeg', 'Peyton Manning': 'peyton2.jpeg', 'Undertaker': 'undertaker2.jpeg', 'Mick Foley': 'foley2.jpeg', 'Pat Mcafee': 'mcafee2.jpeg' }
    text = 'SENDING THIS FROM PYTHON!'
    return render_template('index.html', people = people, athletes_list = athletes_list, artists_list = artists_list)
                                        #keyword = value

@app.route('/athletes')
def athletes():
    athletes_list = {'Reggie Miller': 'reggie2.jpeg', 'Peyton Manning': 'peyton2.jpeg', 'Undertaker': 'undertaker2.jpeg', 'Mick Foley': 'foley2.jpeg', 'Pat Mcafee': 'mcafee2.jpeg' }
    return render_template('athletes.html', athletes_list = athletes_list)

@app.route('/artists')
def artists():
    artists_list = {'Queen': 'queen.jpeg', 'Foo Fighters': 'foo_fighters.jpeg', 'Stephen Sondheim': 'sondheim.jpeg', 'Joe Iconis':'iconis.jpeg', 'Jonathan Larson': 'larson.jpeg'}
    return render_template('artists.html', artists_list = artists_list)
