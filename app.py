from flask import Flask,url_for,render_template
from markupsafe import escape

app = Flask(__name__)

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