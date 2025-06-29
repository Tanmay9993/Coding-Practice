SELECT w1.id, p1.age, w1.coins_needed, w1.power
FROM wands w1
JOIN wands_property p1 ON w1.code = p1.code
WHERE p1.is_evil = 0
  AND w1.coins_needed = (
    SELECT MIN(w2.coins_needed)
    FROM wands w2
    JOIN wands_property p2 ON w2.code = p2.code
    WHERE p2.age = p1.age AND w2.power = w1.power AND p2.is_evil = 0
  )
ORDER BY w1.power DESC, p1.age DESC;



SELECT *
FROM (
    SELECT w.id, p.age, w.coins_needed, w.power,
           ROW_NUMBER() OVER (PARTITION BY p.age, w.power ORDER BY w.coins_needed) AS wor_num
    FROM wands AS w
    JOIN wands_property AS p ON w.code = p.code
    WHERE p.is_evil = 0
) AS ranked_wands
WHERE wor_num = 1
ORDER BY power DESC, age DESC;
