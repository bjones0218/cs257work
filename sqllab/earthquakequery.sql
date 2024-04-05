select quakedate, quaketime, place
from earthquakes
where mag > 5 and latitude between 50 and 100 
;