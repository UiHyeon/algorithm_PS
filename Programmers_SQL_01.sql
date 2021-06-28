SET @hour := -1;

SELECT (@hour := @hour + 1), (SELECT count(hour(DATETIME)) FROM ANIMAL_OUTS where hour(DATETIME) = @hour) as COUNT
FROM ANIMAL_OUTS
where @hour < 23
order by @hour;