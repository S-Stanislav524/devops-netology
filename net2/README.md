1. `ifconfig -a`, `ls /sys/class/net`, `nmcli device status`, `ip link show`  
2. `LLDP`, команда - `lldpctl`  
3. `Virtual Local Area Network`, package - `vlan`  
config netplan:  
```bash
network:
  version: 2
  renderer: networkd
  ethernets: 
    enp2s0f0:
      dhcp4: yes
  vlans:
    vlan3:
      id: 3
      link: enp2s0f0
```
4. `balance-rr`, `balance-xor`, `balance-tlb`, `balance-alb`, `active-backup`, `broadcast`, `link aggregation`  
netplan config;  
```
	network:
	version: 2
	renderer: networkd
	ethernets:
	    eth1:
	        dhcp4: false
	
	    eth2:
	        dhcp4: false
	
	bonds:
	    bond0:
	        dhcp4: false
	        interfaces:
	        - eth1
	        - eth2
	        parameters:
	            mode: balance-rr
	            mii-monitor-interval: 100
```
5. `/29` - 8 адресов.  
можно получить 31 подсеть  
`10.10.10.0/29, 10.10.10.8/29, 10.10.10.16/29, 10.10.10.24/29`  
6. `100.64.0.0/26`
7. Windows - `apr -a, arp -d *, arp -d 10.10.10.1`  
Linux - `ip neigh, ip neigh flush all, ip neigh del 192.168.1.106 dev ens192`  

