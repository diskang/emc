--muslim
select top(1000) fromaccount,count(*) from trade
where toaccount in (1000219,1000039,1000232)
group by fromaccount
order by count(*) desc

select count(*) as freq_of_visit_times from 
	select count(*)as student_visit_times from trade 
	where toaccount=1000019
	group by fromaccount
	order by student_visit_times desc
group by student_visit_times
order by freq_of_visit_times desc