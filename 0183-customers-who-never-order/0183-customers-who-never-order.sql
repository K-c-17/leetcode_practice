# Write your MySQL query statement below
select a.name as Customers
from customers as a
left join orders as b on a.id=b.customerId
where b.customerId is null;