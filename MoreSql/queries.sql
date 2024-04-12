
select t.city, (t.pop/s.pop::float)*100 as state_pop_percentage, s.state
from topCities t
join statePop s
	on s.state = t.state
order by state_pop_percentage desc
;
