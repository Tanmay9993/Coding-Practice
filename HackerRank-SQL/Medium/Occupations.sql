WITH partition_oc AS (
  SELECT name, occupation,
         ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name) AS col_name
  FROM occupations
),
get_doc AS (
  SELECT name AS doctor, col_name FROM partition_oc WHERE occupation = 'Doctor'
),
get_prof AS (
  SELECT name AS professor, col_name FROM partition_oc WHERE occupation = 'Professor'
),
get_sing AS (
  SELECT name AS singer, col_name FROM partition_oc WHERE occupation = 'Singer'
),
get_act AS (
  SELECT name AS actor, col_name FROM partition_oc WHERE occupation = 'Actor'
),
all_rows AS (
  SELECT col_name FROM get_doc
  UNION
  SELECT col_name FROM get_prof
  UNION
  SELECT col_name FROM get_sing
  UNION
  SELECT col_name FROM get_act
)
select d.doctor, p.professor, s.singer, a.actor from all_rows as ar
left join get_doc as d on ar.col_name = d.col_name
left join get_prof as p on ar.col_name = p.col_name
left join get_act as a on ar.col_name = a.col_name
left join get_sing as s on ar.col_name = s.col_name;


-- Output:
-- Aamina Ashley Christeen Eve 
-- Julia Belvet Jane Jennifer 
-- Priya Britney Jenny Ketty 
-- NULL Maria Kristeen Samantha 
-- NULL Meera NULL NULL 
-- NULL Naomi NULL NULL 
-- NULL Priyanka NULL NULL
