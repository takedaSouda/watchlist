from flask import Flask,url_for
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

print('hellow')