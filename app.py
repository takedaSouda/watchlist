from flask import Flask,url_for,render_template
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
import os
import click

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))

class Movie(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(60))
    year=db.Column(db.String(4))


@app.cli.command()
@click.option('--drop',is_flag=True,help='Create after drop.')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@app.cli.command()
def forge():
    db.create_all()
    name='greg li'
    movies=[
        {'title':'My Neighbor Totoro','year':'1988'},
        {'title':'Dead Poets Society','year':'1989'},
        {'title':'A Perfect World','year':'1993'},
        {'title':'Leon','year':'1994'},
        {'title':'Mahjong','year':'1996'},
        {'title':'Swallowtail Butterfly','year':'1996'},
        ]
    user=User(name=name)
    db.session.add(user)
    for m in movies:
        movie=Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo( 'Done.')
    


@app.route('/home')
def hello_world():
    return '<h1>Hello, World!<h1><img src="https://media.giphy.com/media/3o7TKtYXKH8QZqhKQk/giphy.gif">'

@app.route('/user/<username>')
def userpage(username):
    return f'user {escape(username)}'

@app.route('/test')
def test():
    print(url_for('hello_world'))
    q=url_for('userpage',username='miao')
    return f'test page{q}'


movies = [
    {'name':'The Shawshank Redemption','year':'1994'},
    {'name':'The Godfather','year':'1972'},
    {'name':'The Dark Knight','year':'2008'},
    {'name':'12 Angry Men','year':'1957'},
    {'name':'Schindlers List','year':'1993'},
    {'name':'Pulp Fiction','year':'1994'},
    {'name':'The Lord of the Rings: The Return of the King','year':'1999'}
    ]
name='miao'

@app.route('/')
     
def index():
    return render_template('index.html',username=name,movie=movies)

print('hellow')