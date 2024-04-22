import flask
import psycopg2

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def my_sum(num1, num2):
    sum = int(num1) + int(num2)
    return str(sum)

@app.route('/pop/<state>')
def get_pop(state):
    conn = psycopg2.connect(
		host = "localhost",
		port = 5432,
		database = "jonesb2",
		user = "jonesb2",
		password = "card254cup")
    
	state = state.lower()
    
	if conn is not None:
		cur = conn.cursor()

		sql = '''select state, pop
					from statePop
					where lower(code) = %(state)s
					;'''

		cur.execute(sql, {"state":state})
		rows = cur.fetchall()

		if len(rows) == 0:
			return "You did not enter a valid state"
		else:
			return str(rows[0][1])
	else:
		return "Problem with connection"

if __name__ == '__main__':
    my_port = 5116
    app.run(host='0.0.0.0', port = my_port) 