with denorm as (
select json_extract_scalar(_message, '$.firstName') firstName, jobs.* from person
cross join unnest (
  cast(json_extract(_message, '$.jobs') 
  as array(row(job VARCHAR, episode VARCHAR)))) as jobs
)
select * from denorm
where firstName =
(select max(firstName)
 from denorm where job = 'Postman')
 ;
