# Write your MySQL query statement below
with temp as 
(select a.customer_id,b.visit_id,b.amount
from visits as a
left join transactions as b on a.visit_id=b.visit_id
where b.visit_id is null)

select customer_id,count(*) as count_no_trans
from temp
group by customer_id;