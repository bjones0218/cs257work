Drop table if exists topCities;
drop table if exists statePop;

create table topCities(
	city varchar(50),
	state varchar(50),
	pop integer,
	lat real,
	lon real
);

create table statePop(
	code varchar(2),
	state varchar(50),
	pop integer
);

\copy topCities from us-cities-top-1k.csv delimiter ',' csv 
\copy statepop from us-state-pop.csv delimiter ',' csv 