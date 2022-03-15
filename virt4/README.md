1. 
* В режиме `global` служба гарантированно развернет по одной реплике на каждом узле.  
В режиме `replica` служба развернет указанное количество реплик распределенных по кластеру. При этом часть или все реплики могут быть развернуты на одном узле.  
* Используется алгоритм консенсуса raft
* Overlay network - это виртуальная сеть, которую используют контейнеры, распределенная между хостами с запущенным docker
2. ```bash
	[centos@node01 ~]$ sudo docker node ls
	ID                            HOSTNAME             STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
	lssweeiaimkzisfivi2etkdj7 *   node01.netology.yc   Ready     Active         Leader           20.10.13
	jn86adxfx1cjrk5q3m7smz86i     node02.netology.yc   Ready     Active         Reachable        20.10.13
	qr4vzkyktvqca6qao1hwwgeuz     node03.netology.yc   Ready     Active         Reachable        20.10.13
	x4stegc19aqtpn3iq7484hl6k     node04.netology.yc   Ready     Active                          20.10.13
	i9vcbwuinr9cjq5rnjk3t6qvk     node05.netology.yc   Ready     Active                          20.10.13
	w0gcefew2h4pwa54bdme0fn5z     node06.netology.yc   Ready     Active                          20.10.13
   ```
3. ```bash
	[centos@node01 ~]$ sudo docker service ls
	ID             NAME                                MODE         REPLICAS   IMAGE                                          PORTS
	72var4iz62ud   swarm_monitoring_alertmanager       replicated   1/1        stefanprodan/swarmprom-alertmanager:v0.14.0    
	rm79tcze59bc   swarm_monitoring_caddy              replicated   1/1        stefanprodan/caddy:latest                      *:3000->3000/tcp, *:9090->9090/tcp, *:9093-9094->9093-9094/tcp
	eo8s8etiqhxs   swarm_monitoring_cadvisor           global       6/6        google/cadvisor:latest                         
	vg8rwh7pqpn7   swarm_monitoring_dockerd-exporter   global       6/6        stefanprodan/caddy:latest                      
	61hms0hg76sz   swarm_monitoring_grafana            replicated   1/1        stefanprodan/swarmprom-grafana:5.3.4           
	swmvyjgofmrv   swarm_monitoring_node-exporter      global       6/6        stefanprodan/swarmprom-node-exporter:v0.16.0   
	oa56zka5rdr3   swarm_monitoring_prometheus         replicated   1/1        stefanprodan/swarmprom-prometheus:v2.5.0       
	vdgg66vvc8aa   swarm_monitoring_unsee              replicated   1/1        cloudflare/unsee:v0.8.0
   ```
