select quakedate, quaketime, place
from earthquakes
where mag > 5 and latitude between 50 and 100 
;

select quakedate, quaketime, place
from earthquakes
where mag = 1
;

with quake_no as(
	select place, count(id) quakeCount
	from earthquakes
	group by place	
)

select q.place, q.quakeCount
from quake_no q
join (select max(quakeCount) maxQuakes
		from quake_no) as mq
	on mq.maxQuakes = q.quakeCount
