---------------单用户2014年第一学期每月消费总和
--select  top(1000) [fromaccount],-----[toaccount],[syscode],[timestamp],[amount],
--month([timestamp]) as [month],sum([amount])
--from dbo.trade
--where [timestamp]>'2014-09-01 11:27:39.000'
--and [timestamp]<'2015-03-01 11:27:39.000'
--group by [fromaccount],month([timestamp])
--order by [month],[fromaccount]

--select top(100) sum(amount) from dbo.trade 
--where convert(varchar(23),timestamp,23) between '11:00:00' and '13:00:00'
--group by fromaccount ;


--select top(100) ( sum(trade.amount)) as total, account.account,account.gender,account.grade,account.type 
--from dbo.trade as trade join dbo.account as account on trade.fromaccount = account.account
--group by account.account,account.gender,account.grade,account.type
--order by sum(trade.amount) desc;

select sum(trade.amount/100)
from dbo.trade as trade right join dbo.account as account on trade.fromaccount = account.account
where account.gender=1;
select count(*) from account where gender=1;

select sum(trade.amount/100)
from dbo.trade as trade right join dbo.account as account on trade.fromaccount = account.account
where account.gender=0;
select count(*) from account where gender=0;