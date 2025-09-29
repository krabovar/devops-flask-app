from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return(
		 '<p><a href="/about">This is another string!</a></p>'
	       	'<p><a href="/contact">My Email is here!</a></p>'
)
@app.route('/about')
def about():
	return '<p>About Page</p>'

@app.route('/contact')
def contact():
	return '<p>My Email: c23748139@mytudublin.ie</p>'
