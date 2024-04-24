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
	

	if conn is not None:
		cur = conn.cursor()

		nameQuery = '''select name
						from names
						order by Random()
						limit 1'''

		cur.execute(nameQuery)
		rows = cur.fetchall()
		person = rows[0][0]

		adjQuery = '''select adjective
						from adjectives
						order by Random()
						limit 1'''

		cur.execute(adjQuery)
		rows = cur.fetchall()
		word = rows[0][0]

		cityQuery = '''select city
						from topCities
						order by Random()
						limit 1'''
		
		cur.execute(cityQuery)
		rows = cur.fetchall()
		location = rows[0][0]

	randYear = random.randint(1940, 2024)
	return render_template("sentence.html", name = person, adjective = word, city = location, year = randYear)

if __name__ == '__main__':
	my_port = 5116
	app.run(host='0.0.0.0', port = my_port) 