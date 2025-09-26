from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p><a href="/about">Hello, World, I am a Flask app! Click on me!</a></p>'
@app.route('/about')
def about():
	return '<p>About Page</p>'
