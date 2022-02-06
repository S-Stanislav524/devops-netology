1. ```bash 
	 route-views>show ip route 176.99.65.103   
	Routing entry for 176.99.64.0/19
	  Known via "bgp 6447", distance 20, metric 0
	  Tag 6939, type external
	  Last update from 64.71.137.241 1w4d ago
	  Routing Descriptor Blocks:
	  * 64.71.137.241, from 64.71.137.241, 1w4d ago
	      Route metric is 0, traffic share count is 1
	      AS Hops 2
	      Route tag 6939
	      MPLS label: none
   ```
```bash
route-views>show bgp 176.99.65.103   
BGP routing table entry for 176.99.64.0/19, version 276039439
Paths: (22 available, best #21, table default)
  Not advertised to any peer
  Refresh Epoch 1
  20912 3257 9002 44030
    212.66.96.126 from 212.66.96.126 (212.66.96.126)
      Origin IGP, localpref 100, valid, external
      Community: 3257:8052 3257:50001 3257:54900 3257:54901 20912:65004 65535:65284
      path 7FE045336430 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3303 31133 44030
    217.192.89.50 from 217.192.89.50 (138.187.128.158)
      Origin IGP, localpref 100, valid, external
      Community: 3303:1004 3303:1006 3303:1030 3303:1031 3303:3056 65101:1085 65102:1000 65103:276 65104:150
      path 7FE16C4E9788 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  701 3356 20764 44030
    137.39.3.55 from 137.39.3.55 (137.39.3.55)
      Origin IGP, localpref 100, valid, external
      path 7FE0E0B3EE90 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3333 31133 44030
    193.0.0.56 from 193.0.0.56 (193.0.0.56)
      Origin IGP, localpref 100, valid, external
      path 7FE0AC78C970 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  7018 1299 31133 44030
    12.0.1.63 from 12.0.1.63 (12.0.1.63)
      Origin IGP, localpref 100, valid, external
      Community: 7018:5000 7018:37232
      path 7FE0D6494338 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  57866 9002 44030
    37.139.139.17 from 37.139.139.17 (37.139.139.17)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 9002:0 9002:64667
      path 7FE1202AF6C0 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3561 3910 3356 9002 44030
    206.24.210.80 from 206.24.210.80 (206.24.210.80)
      Origin IGP, localpref 100, valid, external
      path 7FE108382E60 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  1351 20764 20764 20764 20764 20764 20764 20764 44030
    132.198.255.253 from 132.198.255.253 (132.198.255.253)
      Origin IGP, localpref 100, valid, external
      path 7FE0E4D85C50 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 2
  8283 31133 44030
    94.142.247.3 from 94.142.247.3 (94.142.247.3)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 8283:1 8283:101 8283:103
      unknown transitive attribute: flag 0xE0 type 0x20 length 0x24
        value 0000 205B 0000 0000 0000 0001 0000 205B
              0000 0005 0000 0001 0000 205B 0000 0005
              0000 0003 
      path 7FE0FF7BCD10 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  20130 6939 44030
    140.192.8.16 from 140.192.8.16 (140.192.8.16)
      Origin IGP, localpref 100, valid, external
      path 7FE04EC42B30 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  4901 6079 31133 44030
    162.250.137.254 from 162.250.137.254 (162.250.137.254)
      Origin IGP, localpref 100, valid, external
      Community: 65000:10100 65000:10300 65000:10400
      path 7FE0EB319DE8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  53767 174 31133 44030
    162.251.163.2 from 162.251.163.2 (162.251.162.3)
      Origin IGP, localpref 100, valid, external
      Community: 174:21101 174:22005 53767:5000
      path 7FE04B8DD998 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3549 3356 9002 44030
    208.51.134.254 from 208.51.134.254 (67.16.168.191)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:2 3356:22 3356:100 3356:123 3356:503 3356:901 3356:2067 3549:2581 3549:30840
      path 7FE045D59E60 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  101 174 31133 44030
    209.124.176.223 from 209.124.176.223 (209.124.176.223)
      Origin IGP, localpref 100, valid, external
      Community: 101:20100 101:20110 101:22100 174:21101 174:22005
      Extended Community: RT:101:22100
      path 7FE0F6E5E048 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3356 9002 44030
    4.68.4.46 from 4.68.4.46 (4.69.184.201)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:2 3356:22 3356:100 3356:123 3356:503 3356:901 3356:2067
      path 7FE0ED5D4470 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 2
  2497 174 31133 44030
    202.232.0.2 from 202.232.0.2 (58.138.96.254)
      Origin IGP, localpref 100, valid, external
      path 7FE173C98350 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  7660 2516 1299 31133 44030
    203.181.248.168 from 203.181.248.168 (203.181.248.168)
      Origin IGP, localpref 100, valid, external
      Community: 2516:1030 7660:9001
      path 7FE16BAC4CA8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  49788 12552 31133 44030
    91.218.184.60 from 91.218.184.60 (91.218.184.60)
      Origin IGP, localpref 100, valid, external
      Community: 12552:12000 12552:12100 12552:12101 12552:22000
      Extended Community: 0x43:100:1
      path 7FE15DB12C10 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  1221 4637 9002 44030
    203.62.252.83 from 203.62.252.83 (203.62.252.83)
      Origin IGP, localpref 100, valid, external
      path 7FE13E4684C8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3257 9002 44030
    89.149.178.10 from 89.149.178.10 (213.200.83.26)
      Origin IGP, metric 10, localpref 100, valid, external
      Community: 3257:8052 3257:50001 3257:54900 3257:54901 65535:65284
      path 7FE16A7BF368 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  6939 44030
    64.71.137.241 from 64.71.137.241 (216.218.252.164)
      Origin IGP, localpref 100, valid, external, best
      path 7FE0BAC06148 RPKI State valid
      rx pathid: 0, tx pathid: 0x0
  Refresh Epoch 1
  19214 3257 9002 44030
    208.74.64.40 from 208.74.64.40 (208.74.64.40)
      Origin IGP, localpref 100, valid, external
      Community: 3257:8791 3257:50001 3257:53100 3257:53101 65535:65284
      path 7FE01D8BAAE8 RPKI State valid
      rx pathid: 0, tx pathid: 0
```
2. 
```bash
~/devops-netology/net3# route
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         _gateway        0.0.0.0         UG    0      0        0 ens192
172.16.0.5      _gateway        255.255.255.255 UGH   0      0        0 ens192
172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
172.22.1.0      0.0.0.0         255.255.255.0   U     0      0        0 br-mailcow
192.168.1.0     0.0.0.0         255.255.255.0   U     0      0        0 ens192
```
3. 
```
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:pop3            0.0.0.0:*               LISTEN      2068632/docker-prox 
tcp        0      0 0.0.0.0:imap2           0.0.0.0:*               LISTEN      2068608/docker-prox 
tcp        0      0 0.0.0.0:sunrpc          0.0.0.0:*               LISTEN      1/init              
tcp        0      0 0.0.0.0:http            0.0.0.0:*               LISTEN      2069886/docker-prox 
tcp        0      0 0.0.0.0:submissions     0.0.0.0:*               LISTEN      2068775/docker-prox 
tcp        0      0 localhost:39381         0.0.0.0:*               LISTEN      1031/containerd     
tcp        0      0 localhost:domain        0.0.0.0:*               LISTEN      987/systemd-resolve 
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN      1061/sshd: /usr/sbi 
tcp        0      0 localhost:19991         0.0.0.0:*               LISTEN      2068524/docker-prox 
tcp        0      0 0.0.0.0:smtp            0.0.0.0:*               LISTEN      2068796/docker-prox 
tcp        0      0 localhost:6010          0.0.0.0:*               LISTEN      3030253/sshd: admin 
tcp        0      0 localhost:13306         0.0.0.0:*               LISTEN      2068202/docker-prox 
tcp        0      0 localhost:6011          0.0.0.0:*               LISTEN      2735714/sshd: admin 
tcp        0      0 0.0.0.0:https           0.0.0.0:*               LISTEN      2069864/docker-prox 
tcp        0      0 0.0.0.0:sieve           0.0.0.0:*               LISTEN      2068538/docker-prox 
tcp        0      0 0.0.0.0:imaps           0.0.0.0:*               LISTEN      2068584/docker-prox 
tcp        0      0 0.0.0.0:pop3s           0.0.0.0:*               LISTEN      2068560/docker-prox 
tcp        0      0 localhost:7654          0.0.0.0:*               LISTEN      2067352/docker-prox 
tcp        0      0 localhost:18983         0.0.0.0:*               LISTEN      2066938/docker-prox 
tcp        0      0 0.0.0.0:submission      0.0.0.0:*               LISTEN      2068753/docker-prox 
```
Пример: На сервер открыты tpc pop3 - 110 порт и imap - 143 для подключения почтовых клиентов. Их слушают контейнер запущенный в docker. PID процессов 2068632 и 2069608.  
4. 
```
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
udp        0      0 localhost:domain        0.0.0.0:*                           987/systemd-resolve 
udp        0      0 0.0.0.0:sunrpc          0.0.0.0:*                           1/init              
udp6       0      0 [::]:sunrpc             [::]:*                              1/init
```
Пример: systemd-resolve - слушает 53 порт (Dns -протокол), выполняет разрешения Dns имен для локальных приложений. ONC RPC (111 порт) протокол слушает служба, преднозначен для корректной работы Nfs.  

5. ![alt text](https://github.com/S-Stanislav524/devops-netology/blob/main/net3/net.jpg?raw=true)


