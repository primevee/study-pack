-- select max values value 
SELECT state, MAX(value) AS max_temp
From temperatures
GROUP BY state
ORDER BY state;
