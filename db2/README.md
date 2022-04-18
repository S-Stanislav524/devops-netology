1. ```
    version: "3.3"
    services:
      postgres:
        image: postgres:12
        environment:
          POSTGRES_DB: "netology"
          POSTGRES_USER: "netology"
          POSTGRES_PASSWORD: "pwdnetology"
          PGDATA: /pgdata
        ports:
          - "5432:5432"
        volumes:
          - pgdata:/pgdata:rw
          - pgbackup:/backup:rw
    volumes:
        pgdata:
        pgbackup:
   ```
2. 
```sql
create database test_db;
\c test_db;

create table orders (
    id        	SERIAL PRIMARY key,
    name        varchar(100) NOT NULL,
    price       integer NOT NULL
);
create table client (
    id        	SERIAL PRIMARY key,
    fname       varchar(100) NOT NULL,
    country     varchar(100) NOT NULL,
    orderId		INTEGER REFERENCES orders (id)
);
CREATE INDEX ON client ((lower(country)));

CREATE user "test-admin-user" with password 'pwdnetology';
GRANT ALL PRIVILEGES ON DATABASE test_db to "test-admin-user"; 
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO "test-admin-user";
-- test-simple-user
CREATE USER "test-simple-user" WITH PASSWORD 'pwdnetology';
GRANT UPDATE, SELECT, INSERT, DELETE ON ALL TABLES IN SCHEMA public TO "test-simple-user";
```
```
SELECT datname FROM pg_database;
postgres
netology
template1
template0
test_db
```
```
test_db=# \d orders
                                    Table "public.orders"
 Column |          Type          | Collation | Nullable |              Default               
--------+------------------------+-----------+----------+------------------------------------
 id     | integer                |           | not null | nextval('orders_id_seq'::regclass)
 name   | character varying(100) |           | not null | 
 price  | integer                |           | not null | 
Indexes:
    "orders_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "client" CONSTRAINT "client_orderid_fkey" FOREIGN KEY (orderid) REFERENCES orders(id)

test_db=# \d client
                                    Table "public.client"
 Column  |          Type          | Collation | Nullable |              Default               
---------+------------------------+-----------+----------+------------------------------------
 id      | integer                |           | not null | nextval('client_id_seq'::regclass)
 fname   | character varying(100) |           | not null | 
 country | character varying(100) |           | not null | 
 orderid | integer                |           |          | 
Indexes:
    "client_pkey" PRIMARY KEY, btree (id)
    "client_lower_idx" btree (lower(country::text))
Foreign-key constraints:
    "client_orderid_fkey" FOREIGN KEY (orderid) REFERENCES orders(id)

test_db=# \z
                                           Access privileges
 Schema |     Name      |   Type   |         Access privileges          | Column privileges | Policies 
--------+---------------+----------+------------------------------------+-------------------+----------
 public | client        | table    | netology=arwdDxt/netology         +|                   | 
        |               |          | "test-admin-user"=arwdDxt/netology+|                   | 
        |               |          | "test-simple-user"=arwd/netology   |                   | 
 public | client_id_seq | sequence |                                    |                   | 
 public | orders        | table    | netology=arwdDxt/netology         +|                   | 
        |               |          | "test-admin-user"=arwdDxt/netology+|                   | 
        |               |          | "test-simple-user"=arwd/netology   |                   | 
 public | orders_id_seq | sequence |                                    |                   | 
(4 rows)
```
```
SELECT * FROM information_schema.table_privileges
where table_catalog = 'test_db';
```
3. 
```
INSERT INTO public.orders
("name", price)
VALUES('шоколад', 10),
('Принтер', 3000),
('Книга', 500),
('Монитор', 7000),
('Гитара', 4000);
INSERT INTO public.client
(fname, country, orderid)
VALUES('Иванов Иван Иванович', 'usa', null),
('Иванов Иван Иванович', 'usa', null),
('Петров Петр Петрович', 'Canada', null),
('Иоганн Себастьян Бах', 'japan', null),
('Ронни Джеймс Дио', 'Russia', null),
('Ritchie Blackmore', 'Russia', null);
```
```
test_db=# select count(*) from orders; 
 count 
-------
     5
```
```
test_db=# select count(*) from client; 
 count 
-------
     6
```
4. 
```
UPDATE public.client
SET orderid=(select id from orders where name = 'Книга')
WHERE fname = 'Иванов Иван Иванович';
UPDATE public.client
SET orderid=(select id from orders where name = 'Монитор')
WHERE fname = 'Петров Петр Петрович';
UPDATE public.client
SET orderid=(select id from orders where name = 'Гитара')
WHERE fname = 'Иоганн Себастьян Бах';
```
```
test_db=# select c.fname, o."name"  from client c 
        inner join orders o on c.orderid = o.id;
        fname         |  name   
----------------------+---------
 Иванов Иван Иванович | шоколад
 Иоганн Себастьян Бах | Гитара
 Петров Петр Петрович | Монитор
(3 rows)

```
5.
```
test_db=# explain select c.fname, o."name"  from client c 
        inner join orders o on c.orderid = o.id;
                               QUERY PLAN                                
-------------------------------------------------------------------------
 Hash Join  (cost=17.20..29.36 rows=170 width=436)
   Hash Cond: (c.orderid = o.id)
   ->  Seq Scan on client c  (cost=0.00..11.70 rows=170 width=222)
   ->  Hash  (cost=13.20..13.20 rows=320 width=222)
         ->  Seq Scan on orders o  (cost=0.00..13.20 rows=320 width=222)
(5 rows)

```
Hash join - ланировщик выбирает соединение по хешу, при котором строки одной таблицы записываются в хеш-таблицу в памяти, после чего сканируется другая таблица и для каждой её строки проверяется соответствие по хеш-таблице  
cost - стоимость запуска; время которое проходит от начала запуска до вывода данных    
rows - ожижаемое количество строк   
width - ожидаемый средний размер строк  
Вначале по полученным данным из orders конструируется хэш-таблица, далее она передается узлу Hash Join, который читает строки из узла внешнего потомка и проверяет их по этой хеш-таблице. 

6. 
```
pg_dump -c -U netology test_db > /backup/db.dump
pg_restore -U netology -C -d test_db -Ft /backup/db.dump
```

