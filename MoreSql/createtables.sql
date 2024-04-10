Drop table if exists topCities;
drop table if exists statePop;

create table topCities(
	city varchar(25),
	state varchar(25),
	pop integer,
	lat real,
	lon real
);

create table statePop(
	code varchar(2),
	state varchar(25),
	pop integer
);

