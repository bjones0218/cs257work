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
		
		return True
	else:
		print("Problem with connection")
		return False



def runQueryTwo():
	conn = psycopg2.connect(
		host = "localhost",
		port = 5432,
		database = "jonesb2",
		user = "jonesb2",
		password = "card254cup")
	
	if conn is not None:
		cur = conn.cursor()

		sql = "select c.city from topCities c join (select max(pop) as maxPop from topCities) as m on c.pop = m.maxPop"

		cur.execute(sql)
		rows = cur.fetchall()

		if len(rows) == 0:
			print("There is a problem with your query")
		else:
			for each in rows:
				print(each[0])
		
		return True
	else:
		print("Problem with connection")
		return False

def runQueryThree():
	conn = psycopg2.connect(
		host = "localhost",
		port = 5432,
		database = "jonesb2",
		user = "jonesb2",
		password = "card254cup")
	
	if conn is not None:
		cur = conn.cursor()

		sql = "select c.city from topCities c join (select min(pop) as minPop from topCities where state like 'Minnesota') as m on c.pop = m.minPop where c.state like 'Minnesota'"

		cur.execute(sql)
		rows = cur.fetchall()

		if len(rows) == 0:
			print("There is a problem with your query")
		else:
			for each in rows:
				print(each[0])
		
		return True
	else:
		print("Problem with connection")
		return False

# runQueryOne()
# runQueryTwo()
runQueryThree()