import psycopg2

def createtables():
	conn = psycopg2.connect(
		host = "localhost",
		port = 5432,
		database = "jonesb2",
		user = "jonesb2",
		password = "card254cup")
	
	if conn is not None:
		cur = conn.cursor()

		sql = "create table topCities(city varchar(50), state varchar(50), pop integer, lat real, lon real); create table statePop(code varchar(2), state varchar(50), pop integer);"

		cur.execute(sql)
		conn.commit()
		print("Your tables have been created")
	else:
		print("Problem with connection")

	return True;