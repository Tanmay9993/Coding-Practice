
# Write your MySQL query statement below

select start_act.machine_id as machine_id, round(avg(stop_act.timestamp- start_act.timestamp),3) as processing_time  from
Activity as start_act
left Join Activity as stop_act
on start_act.machine_id = stop_act.machine_id
and start_act.process_id = stop_act.process_id
where start_act.activity_type = 'start'
and stop_act.activity_type = 'end'
group by start_act.machine_id;



-- select start_act.machine_id as m_id, start_act.process_id as p_id, start_act.activity_type as act_start, stop_act.activity_type as act_stop, start_act.timestamp as start_time,  stop_act.timestamp as stop_time from
-- Activity as start_act
-- left Join Activity as stop_act
-- on start_act.machine_id = stop_act.machine_id
-- and start_act.process_id = stop_act.process_id
-- where start_act.activity_type = 'start'
-- and stop_act.activity_type = 'end';
