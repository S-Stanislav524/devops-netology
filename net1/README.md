1. `HTTP/1.1 301 Moved Permanently` - запрошенный документ был окончательно перенесен на новый URI, указанный в поле Location заголовка
2. запрос `GET	http://stackoverflow.com/` был самым долгим 692 мс  
![alt text](https://github.com/S-Stanislav524/devops-netology/blob/main/net1/screen.jpg?raw=true)
4. `176.99.65.103`
5. `OtradnoeNet Ltd.`, `AS44030`
6. ```bash
	root@k8s:~/devops-netology# traceroute -An 8.8.8.8
	traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
	 1  192.168.1.2 [*]  0.394 ms  0.298 ms  0.294 ms
	 2  176.99.65.254 [AS44030]  1.243 ms  1.171 ms  1.218 ms
	 3  176.99.94.62 [AS44030]  1.558 ms  1.673 ms  2.073 ms
	 4  176.99.94.36 [AS44030]  1.660 ms  1.666 ms  1.641 ms
	 5  176.99.94.41 [AS44030]  2.097 ms  2.211 ms  2.081 ms
	 6  176.99.94.5 [AS44030]  1.824 ms  1.657 ms  1.637 ms
	 7  176.99.94.110 [AS44030]  1.756 ms  1.821 ms  1.810 ms
	 8  74.125.244.181 [AS15169]  3.654 ms 74.125.244.133 [AS15169]  1.913 ms 74.125.244.181 [AS15169]  3.556 ms
	 9  142.251.61.221 [AS15169]  6.243 ms 72.14.232.84 [AS15169]  3.684 ms  3.698 ms
	10  216.239.48.163 [AS15169]  5.320 ms 142.250.56.217 [AS15169]  7.352 ms 142.251.61.219 [AS15169]  5.872 ms
	11  * * *
	12  * * *
	13  * * *
	14  * * *
	15  * * *
	16  * * *
	17  * * *
	18  * * *
	19  * * *
	20  8.8.8.8 [AS15169]  5.327 ms  5.478 ms *
   ```
6. `AS15169  216.239.63.65` - 6,2 мс
7. `dig dns.google ns`  
```
dns.google.		21600	IN	NS	ns2.zdns.google.
dns.google.		21600	IN	NS	ns1.zdns.google.
dns.google.		21600	IN	NS	ns4.zdns.google.
dns.google.		21600	IN	NS	ns3.zdns.google.
```
`dig dns.google.com`
```
dns.google.		210	IN	A	8.8.4.4
dns.google.		210	IN	A	8.8.8.8
```
8. `dig -x 8.8.4.4`  
`4.4.8.8.in-addr.arpa.	19662	IN	PTR	dns.google.`  
`dig -x 8.8.4.4`  
`8.8.8.8.in-addr.arpa.	6437	IN	PTR	dns.google.`  


