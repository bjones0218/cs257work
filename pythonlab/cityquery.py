import psycopg2

def runQueryOne():
	conn = psycopg2.connect(
		host = "localhost",
		port = 5432,
		database = "jonesb2",
		user = "jonesb2",
		password = "card254cup")
	
	if conn is not None:
		cur = conn.cursor()

		sql = "select * from topCities where city like 'Northfield' and state like 'Minnesota'"

		cur.execute(sql)
		rows = cur.fetchall()

		if len(rows) == 0:
			print("Northfield is not in this database.")
		else:
			print("The latitude is " + rows[0][3] + " and the longitude is " + rows[0][4])
	else:
		print("Problem with connection")

	return True

runQueryOne()