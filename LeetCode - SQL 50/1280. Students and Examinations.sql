# Write your MySQL query statement below

with exams as (select s.student_id as student_id, e.student_id as e_stu,  e.subject_name as actual, sb.subject_name as subject_name,
case when e.subject_name = sb.subject_name 
then 1
else 0
end as exams_attended 
from Examinations as e
right join Students as s on e.student_id = s.student_id
cross join subjects as sb )



select ex.student_id, s.student_name, ex.subject_name, sum(ex.exams_attended) as attended_exams 
from exams as ex
join Students as s 
on s.student_id = ex.student_id
group by ex.student_id, ex.subject_name
order by ex.student_id, ex.subject_name;


