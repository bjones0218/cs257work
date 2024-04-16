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

def runQueryFour():
	conn = psycopg2.connect(
		host = "localhost",
		port = 5432,
		database = "jonesb2",
		user = "jonesb2",
		password = "card254cup")
	
	if conn is not None:
		cur = conn.cursor()

		sql = '''with maxNorth as (
					select max(lat) as mostNorth 
					from topCities
				),
				maxSouth as (
					select min(lat) as mostSouth
					from topCities
				),
				maxEast as (
					select max(lon) as mostEast
						from topCities
				), 
				maxWest as (
					select min(lon) as mostWest
						from topCities
				)
				select * from maxNorth
				;'''

					# select topCities.city 
					# from topCities 
					# join maxNorth 
					# 	on maxNorth.mostNorth = topCities.lat 
					# join maxSouth 
					# 	on maxSouth.mostSouth = topCities.lat 
					# join maxEast 
					# 	on maxEast.mostEast = topCities.lon 
					# join maxWest 
					# 	on maxWest.mostWest = topCities.lon

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
# runQueryThree()
runQueryFour()