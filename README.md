# 1 SQL-запрос
SELECT c.login, COUNT (o.in_Delivery)
FROM "Couries" AS c
INNER JOIN "Orders" AS o ON c.id=o.courierId;

# 2 SQL-запрос
SELECT track
CASE WHEN finished IS true THEN = 2
           WHEN cancelled IS true THEN = -1
           WHEN inDelivery IS true THEN = 1
           ELSE = 0 
FROM "Orders";
