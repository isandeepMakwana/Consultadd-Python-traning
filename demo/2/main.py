# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
	return 'Hello World'


if __name__ == '__main__':

	app.run(debug=True , ports=2900)
    

