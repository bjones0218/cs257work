from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template("index.html")

@app.route('/rand_sentence')
def rand():
	#	Input values that come from a URL (i.e., @app.route)
	#   are always strings so I need to convert the type to int
 
	conn = psycopg2.connect(
		host = "localhost",
		port = 5432,
		database = "jonesb2",
		user = "jonesb2",
		password = "card254cup")
	

	

	randYear = random.randint(1940, 2024)
	return render_template("sentence.html", name = person, adjective = word, city = location, year = randYear)

if __name__ == '__main__':
	my_port = 5116
	app.run(host='0.0.0.0', port = my_port) 