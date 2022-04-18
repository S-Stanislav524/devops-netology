1.
```bash
ysql> \s
--------------
mysql  Ver 8.0.28 for Linux on x86_64 (MySQL Community Server - GPL)

Connection id:          13
Current database:
Current user:           root@localhost
SSL:                    Not in use
Current pager:          stdout
Using outfile:          ''
Using delimiter:        ;
Server version:         8.0.28 MySQL Community Server - GPL
Protocol version:       10
Connection:             Localhost via UNIX socket
Server characterset:    utf8mb4
Db     characterset:    utf8mb4
Client characterset:    latin1
Conn.  characterset:    latin1
UNIX socket:            /var/run/mysqld/mysqld.sock
Binary data as:         Hexadecimal
Uptime:                 8 min 18 sec
```
```sql
\r testbd

mysql> SELECT table_name FROM information_schema.tables WHERE table_schema = 'test_db';
+------------+
| TABLE_NAME |
+------------+
| orders     |
+------------+

mysql> select count(*) from orders where price > 300;
+----------+
| count(*) |
+----------+
|        1 |
+----------+
```
2.
```sql
CREATE USER 'test'@'localhost' IDENTIFIED BY 'test-pass';
ALTER USER 'test'@'localhost' PASSWORD EXPIRE INTERVAL 180 DAY;
ALTER USER 'test'@'localhost' FAILED_LOGIN_ATTEMPTS 3;
ALTER USER 'test'@'localhost' IDENTIFIED WITH mysql_native_password;
ALTER USER 'test'@'localhost' WITH MAX_QUERIES_PER_HOUR 100;
ALTER USER 'test'@'localhost' ATTRIBUTE '{"fname": "James", "lname": "Pretty"}';

GRANT SELECT ON test_db.* TO 'test'@'localhost';

mysql> select  * from INFORMATION_SCHEMA.USER_ATTRIBUTES where user = 'test';
+------+-----------+---------------------------------------+
| USER | HOST      | ATTRIBUTE                             |
+------+-----------+---------------------------------------+
| test | localhost | {"fname": "James", "lname": "Pretty"} |
+------+-----------+---------------------------------------+
1 row in set (0.01 sec)
```
3.
```sql
mysql> SHOW TABLE STATUS FROM test_db \G;
*************************** 1. row ***************************
           Name: orders
         Engine: InnoDB
        Version: 10
     Row_format: Dynamic
           Rows: 5
 Avg_row_length: 3276
    Data_length: 16384
Max_data_length: 0
   Index_length: 0
      Data_free: 0
 Auto_increment: 6
    Create_time: 2022-04-18 17:11:45
    Update_time: 2022-04-18 17:11:45
     Check_time: NULL
      Collation: utf8mb4_0900_ai_ci
       Checksum: NULL
 Create_options: 
        Comment: 
```
* innoDB
```sql
mysql> show profiles;
+----------+------------+-----------------------------------------------+
| Query_ID | Duration   | Query                                         |
+----------+------------+-----------------------------------------------+
|       11 | 0.07843300 | ALTER TABLE orders ENGINE = InnoDB            |
|       12 | 0.00065825 | select count(*) from orders where price > 300 |
+----------+------------+-----------------------------------------------+
2 rows in set, 1 warning (0.00 sec)
```
* MyISAM
```sql
mysql> show profiles;
+----------+------------+-----------------------------------------------+
| Query_ID | Duration   | Query                                         |
+----------+------------+-----------------------------------------------+
|        8 | 0.00057600 | select count(*) from orders where price > 300 |
+----------+------------+---------------------------------------
```
4.
```
[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
secure-file-priv= NULL

# Custom config should go here
!includedir /etc/mysql/conf.d/
innodb_buffer_pool_size = 1536M
innodb_log_buffer_size = 1M
innodb_flush_method = O_DSYNC
innodb_flush_log_at_trx_commit = 1
innodb_log_file_size = 100M
innodb_file_per_table
innodb_file_format = Barracuda
```
