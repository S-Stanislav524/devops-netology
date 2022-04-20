1.
* вывода списка БД - `\l`
* подключения к БД - `\conninfo`
* вывода списка таблиц - `\dt`
* вывода описания содержимого таблиц `\d+`
* выхода из psql - `\q`
2. * `CREATE DATABASE test_batabase;`, `psql -U netology -d test_database < /backup/test_dump.sql`
```sql
SELECT attname,avg_width from pg_stats WHERE tablename = 'orders' and avg_width = (SELECT MAX(avg_width) from pg_stats WHERE tablename = 'orders');
 attname | avg_width 
---------+-----------
 title   |        16
(1 row)
```
3. * 
```sql
CREATE TABLE orders_1 (CHECK (price > 499)) INHERITS (orders);
CREATE TABLE orders_2 (CHECK (price <= 499)) INHERITS (orders);
CREATE RULE new_insert_to_1 AS ON INSERT TO orders where (price >499) DO INSTEAD INSERT INTO orders_1 VALUES (NEW.*);
CREATE RULE new_insert_to_2 AS ON INSERT TO orders where (price <=499) DO INSTEAD INSERT INTO orders_2 VALUES (NEW.*);
START TRANSACTION;
BEGIN;
CREATE TEMP TABLE temp_table ON COMMIT DROP AS (SELECT * FROM orders);
DELETE FROM orders;
INSERT INTO orders (id,title,price) SELECT id,title,price FROM temp_table;
COMMIT;
```
* можно ели бы при создании таблицы было бы указано `PARTITION BY RANGE (price);`
```sql
ALTER TABLE orders_1 ADD CONSTRAINT orders_1_ UNIQUE (title, price);
ALTER TABLE orders_2 ADD CONSTRAINT orders_2_ UNIQUE (title, price);
```