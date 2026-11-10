-- Write your query below
SELECT name from customers WHERE ID NOT IN (SELECT customer_id from orders);