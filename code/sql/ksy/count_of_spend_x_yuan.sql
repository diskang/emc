select a.stu_total/b.liveday_count/100 as daily_spend,count(*)
from (select fromaccount,sum(amount) as stu_total
	from emc.dbo.trade
	group by fromaccount)a
join
--get get active date count per student
	(select fromaccount,count(distinct convert(varchar,timestamp, 23)) as liveday_count
		from emc.dbo.trade 
		group by fromaccount)b
on a.fromaccount = b.fromaccount
where liveday_count>=20
group by a.stu_total/b.liveday_count/100
order by daily_spend



-- difference between male and female

select a.stu_total/b.liveday_count/100 as daily_spend,count(*)
from (select fromaccount,sum(amount) as stu_total
	from emc.dbo.trade
	group by fromaccount)a

join

--get get active date count per student
	(select fromaccount,count(distinct convert(varchar,timestamp, 23)) as liveday_count
		from emc.dbo.trade 
		group by fromaccount)b

on a.fromaccount = b.fromaccount 
left join emc.dbo.account on a.fromaccount = account.account
where liveday_count>=20 and account.gender=1
group by a.stu_total/b.liveday_count/100

order by daily_spend