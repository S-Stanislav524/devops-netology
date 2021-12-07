1. ```bash
	wget https://github.com/prometheus/node_exporter/releases/download/v1.3.0/node_exporter-1.3.0.linux-amd64.tar.gz
	tar xvfz node_exporter-*.*-amd64.tar.gz
	cd node_exporter-*.*-amd64
	ln ./node_exporter /usr/sbin
	cat /lib/systemd/system/node_exporter.service
   ```
   ```
	[Unit]
	Description=Node Exporter
	
	[Service]
	EnvironmentFile=-/etc/node_exporter.conf
	KillMode=process
	ExecStart=/usr/sbin/node_exporter
	Restart=Always
	
	[Install]
	WantedBy=default.target
   ```  
   ```bash
	systemctl enable node_exporter.service
	systemctl start node_exporter.service
	systemctl status node_exporter.service
   ```
2. ```bash 
	node_cpu_seconds_total
   	node_pressure_cpu_waiting_seconds_total
	process_cpu_seconds_total
	node_memory_Active_bytes
	node_memory_MemFree_bytes
	node_memory_SwapFree_bytes 
	node_filesystem_free_bytes
	node_filesystem_avail_bytes
	node_disk_io_now
	node_network_receive_bytes_total
   ```
3. Выполнено
4. Можно по следующим сообщениям `Booting paravirtualized kernel on VMware hypervisor`
5. `fs.nr_open` - это системное ограничение на количество дескрипторов файла, которые может выделить процесс. 
По умолчанию 1048576.  
Такого числа не позволяет достичь "soft" лимит установленный в системе по умолчанию для пользователяю.  
Его можно посмотреть через команду `ulimiy -Sn` 
6. ```bash 
	unshare -f --pid  --mount-proc /bin/sleep 1h &
	ps -e | grep sleep
	374228 pts/3    00:00:00 sleep
	nsenter -p 374228 -p -r ps -ex
	PID TTY      STAT   TIME COMMAND
     	 1 pts/3    S+     0:00 /bin/sleep 1h SHELL=/bin/bash SUDO_GID=1000 SUDO_COMMAN
     	 2 pts/3    R+     0:00 ps -ex SHELL=/bin/bash SUDO_GID=1000 SUDO_COMMAND=/bin/

   ```
7. `cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-21.scope`  
Сработало ограничение ресурсов внутри cgroups по количеству pid.
изменить можно через `echo 123 > /sys/fs/cgroup/pids/user.slice/user-1000.slice/user@1000.service/pids.max` 
или `ulimit -u 123`

