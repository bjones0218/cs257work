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

		sql = '''select c.city 
					from topCities c 
					join (
						select min(pop) as minPop 
							from topCities 
							where state like 'Minnesota') as m 
						on c.pop = m.minPop 
					where c.state like 'Minnesota' 
				; '''

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
				),
				allTogether as(
					select topCities.city, topCities.state, 'North' as direction
						from topCities 
						join maxNorth 
							on maxNorth.mostNorth = topCities.lat 
					union all
					select topCities.city, topCities.state, 'South' as direction
						from topCities 
						join maxSouth 
							on maxSouth.mostSouth = topCities.lat 				
					union all
					select topCities.city, topCities.state, 'East' as direction
						from topCities 
						join maxEast 
							on maxEast.mostEast = topCities.lon 	
					union all
					select topCities.city, topCities.state, 'West' as direction
						from topCities 
						join maxWest 
							on maxWest.mostWest = topCities.lon
				)
				select *
					from allTogether					
				;'''

		cur.execute(sql)

		for row in cur:
			print(row)

		return True
	else:
		print("Problem with connection")
		return False

def runQueryFive():
	conn = psycopg2.connect(
		host = "localhost",
		port = 5432,
		database = "jonesb2",
		user = "jonesb2",
		password = "card254cup")
	
	if conn is not None:
		cur = conn.cursor()

		state = input('Enter a state from the United States: ').lower()
		
		if len(state) == 2:
			sql = '''with stateName as (
						select state
						from statePop
						where lower(code) = %(state)s
					) 
					select topCities.state, sum(pop) as totalPopulation
					from topCities
					join stateName 
						on stateName.state = topCities.state 
					group by topCities.state
					;'''
		else:
			sql = '''with citiesInState as (
						select * 
						from topCities 
						where lower(state) = %(state)s
					)
					select citiesInState.state, 
						   sum(pop) as totalPopulation
						from citiesInState
						group by state'''

		cur.execute(sql, {"state":state})	

		if len(cur) == 0:
			print('You did not enter a valid state or state code.')
		else:
			for row in cur:
				print(row)
		
		return True
	else:
		print("Problem with connection")
		return False

# runQueryOne()
# runQueryTwo()
# runQueryThree()
# runQueryFour()
runQueryFive()