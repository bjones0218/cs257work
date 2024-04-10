
select t.city, (t.pop / s.pop) as state_pop_proportion
from topCities t
join statePop s
	on s.state = t.state
order by state_pop_proportion
limit 10
;
