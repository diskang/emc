
select (amount/50)/2.0 as yuan, count(amount/50) as perchase_count
from emc.dbo.trade
group by (amount/50)
order by yuan

select (amount/100) as yuan, count(amount/100) as perchase_count
from emc.dbo.trade
group by (amount/100)
order by yuan

select (amount/100) as amt, count(amount/100) as perchase_count 
from emc.dbo.trade
where toaccount = '1000029'
group by (amount/100)
order by amt