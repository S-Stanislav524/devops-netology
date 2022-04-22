1. * 
```
FROM centos:7
RUN groupadd --gid 2000 node \
  && useradd --uid 2000 --gid node --shell /bin/bash --create-home node
ADD elasticsearch-8.1.2-darwin-x86_64.tar.gz /data
ADD openjdk-18.0.1_linux-x64_bin.tar.gz /data
ENV ES_JAVA_HOME /data/jdk-18.0.1
ENV ES_JAVA_OPTS "-Xms2g -Xmx2g" 
WORKDIR /data/
RUN echo -e "path.data: /var/lib \nnode.name: netology_test \nhttp.port: 9200 \nxpack.ml.enabled: false" >> ./elasticsearch-8.1.2/config/elasticsearch.yml &&\
    echo -e "node.roles: [ master, data ]" >> ./elasticsearch-8.1.2/config/elasticsearch.yml &&\
    chown -R node:node /data && \
    chown node:node /var/lib
EXPOSE 9200
USER node
CMD [ "/data/elasticsearch-8.1.2/bin/elasticsearch" ]
```
* `docker pull wwqq/elastic:1.0`
* 
```bash
~/devops-netology/db5$ curl http://localhost:9200 
{
  "name" : "netology_test",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "jzQ8qMKxS6O2Ijqnv9us_g",
  "version" : {
    "number" : "8.1.2",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "31df9689e80bad366ac20176aa7f2371ea5eb4c1",
    "build_date" : "2022-03-29T21:18:59.991429448Z",
    "build_snapshot" : false,
    "lucene_version" : "9.0.0",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```
2. 
```bash 
curl http://localhost:9200/_cat/indices
green  open ind-1 JzI4jX_kRzG6AxdFS6eptA 1 0 0 0 225b 225b
yellow open ind-3 c1553GeXREqLtf1Etvqkug 4 2 0 0 900b 900b
yellow open ind-2 XR9oABn9SLSJXjvqKdAu7w 2 1 0 0 450b 450b
```
```bash
curl http://localhost:9200/_cluster/health?pretty=true
{
  "cluster_name" : "elasticsearch",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 8,
  "active_shards" : 8,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 10,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 44.44444444444444
}
```
* Как вы думаете, почему часть индексов и кластер находится в состоянии yellow? - Потому что количесто используется 1 нода и количество реплик не может быть больше нуля
```bash
curl -X DELETE "http://localhost:9200/ind-1"
curl -X DELETE "http://localhost:9200/ind-2"
curl -X DELETE "http://localhost:9200/ind-3"
```
3.
```
curl -XPUT 'http://localhost:9200/_snapshot/netology_backup' -H 'Content-Type: application/json' -d '{
    "type": "fs",
    "settings": {
        "location": "snapshot repository",
        "compress": true
    }
}'
{"acknowledged":true}
```
```
curl -H 'Content-Type: application/json' -XPUT "$ES_URL/ind-1" -d'
{
  "settings": {
    "index": {
      "number_of_shards": 1,  
      "number_of_replicas": 0 
    }
  }
}'
{"acknowledged":true,"shards_acknowledged":true,"index":"ind-1"}

curl http://localhost:9200/_cat/indices
green open ind-1 _1PhlkPNSyCFiORU5R6OTA 1 0 0 0 225b 225b
```
`curl -XPUT http://localhost:9200/_snapshot/netology_backup/%3Cmy_snapshot_%7Bnow%2Fd%7D%3E`
```bash 
[node@447e327e5a11 data]$ ls -la ./elasticsearch-8.1.2/snapshots/snapshot\ repository/
total 40
drwxr-xr-x 3 node node  4096 Apr 20 12:14 .
drwxr-xr-x 1 node node  4096 Apr 20 12:06 ..
-rw-r--r-- 1 node node   856 Apr 20 12:14 index-0
-rw-r--r-- 1 node node     8 Apr 20 12:14 index.latest
drwxr-xr-x 4 node node  4096 Apr 20 12:14 indices
-rw-r--r-- 1 node node 16375 Apr 20 12:14 meta-_m8MkvimTziJ-Cb-34e4jQ.dat
-rw-r--r-- 1 node node   366 Apr 20 12:14 snap-_m8MkvimTziJ-Cb-34e4jQ.dat
```
```bash
curl -X POST  $ES_URL/_snapshot/netology_backup/my_snapshot_2022.04.20/_restore -H 'Content-Type: application/json' -d '{
  "indices": "ind-1"
}'
{"accepted":true}

curl http://localhost:9200/_cat/indices
green open ind-1 lMktapaJQm2tMG5C7LujJA 1 0 0 0 225b 225b
green open ind-2 YDUTxNY1SbWrgV0jMTcLlw 1 0 0 0 225b 225b
```