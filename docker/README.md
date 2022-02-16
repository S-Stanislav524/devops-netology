1. https://hub.docker.com/repository/docker/wwqq/nginx
2. Для всех случаев подойдет docker. Во всех случаях перимуществами будет легкость разворачивания, обновления и миграции контейнеров, уменьшение затрат на ресурсов на слои виртуализации, т.к. используется ядро хостовой ОС; Возможность быстрого масштабирования в ширину. Для каждой из задачь есть уже готовые image в котовые необходимо добавить только свои настройки или артефакты. 
* Высоконагруженное монолитное java веб-приложение
* Nodejs веб-приложение;  
* Мобильное приложение c версиями для Android и iOS - есть готовые образы docker для Andoid и iOS
* Шина данных на базе Apache Kafka;
* Elasticsearch кластер для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana;
* Мониторинг-стек на базе Prometheus и Grafana;
* MongoDB, как основное хранилище данных для java-приложения;
* Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry.  
3. ```bash
   mkdir ./data
   docker run -d -v $(pwd)/data:/data centos 
   docker run -d -v $(pwd)/data:/data centos 
   docker ps
   CONTAINER ID   IMAGE     COMMAND            CREATED          STATUS          PORTS     NAMES
    a40714d3df4c   centos    "/bin/sleep 999"   13 seconds ago   Up 12 seconds             busy_lehmann
    bb7f93a1edfc   centos    "/bin/sleep 999"   6 minutes ago    Up 6 minutes              pensive_mcclintock
   docker exec -it a40714d3df4c /bin/bash
   [root@a40714d3df4c /]# touch /data/testfile.txt 
   [root@a40714d3df4c /]# exit
   touch ./data/test2.txt
   docker exec -it bb7f93a1edfc /bin/bash
   [root@bb7f93a1edfc /]# ls -la /data
    total 8
    drwxr-xr-x 2 root root 4096 Feb 16 10:14 .
    drwxr-xr-x 1 root root 4096 Feb 16 10:09 ..
    -rw-r--r-- 1 root root    0 Feb 16 10:14 test2.txt
    -rw-r--r-- 1 root root    0 Feb 16 10:10 testfile.txt
   ```