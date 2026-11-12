-- Write your query below
SELECT seller_name from seller s
where seller_id NOT IN
(SELECT seller_id from orders WHERE sale_date >= '2020-01-01' AND sale_date <= '2020-12-31')
ORDER BY s.seller_name ASC;