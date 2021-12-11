1. Выполнено
2. Нет не может, т.к. жесткая ссылка и файл, для которого она создавалась имеют одинаковые inode, поэтому она имеет теже права доступа, владельцп
 и время последней модификации. Различаются только имена файлов.
3. `fdisk -l`  
```	Disk /dev/sda: 2.5 GiB, 2684354560 bytes, 5242880 sectors
	Disk model: Virtual disk    
	Units: sectors of 1 * 512 = 512 bytes
	Sector size (logical/physical): 512 bytes / 512 bytes
	I/O size (minimum/optimal): 512 bytes / 512 bytes

	Disk /dev/sdb: 2.5 GiB, 2684354560 bytes, 5242880 sectors
	Disk model: Virtual disk    
	Units: sectors of 1 * 512 = 512 bytes
	Sector size (logical/physical): 512 bytes / 512 bytes
	I/O size (minimum/optimal): 512 bytes / 512 bytes
```
4. 
```bash
	root@k8s:~/devops-netology# fdisk /dev/sda
	
	Welcome to fdisk (util-linux 2.36).
	Changes will remain in memory only, until you decide to write them.
	Be careful before using the write command.
	
	Device does not contain a recognized partition table.
	Created a new DOS disklabel with disk identifier 0x61e952fa.
	
	Command (m for help): p
	Disk /dev/sda: 2.5 GiB, 2684354560 bytes, 5242880 sectors
	Disk model: Virtual disk    
	Units: sectors of 1 * 512 = 512 bytes
	Sector size (logical/physical): 512 bytes / 512 bytes
	I/O size (minimum/optimal): 512 bytes / 512 bytes
	Disklabel type: dos
	Disk identifier: 0x61e952fa
	
	Command (m for help): n
	Partition type
	   p   primary (0 primary, 0 extended, 4 free)
	   e   extended (container for logical partitions)
	Select (default p): 

	Using default response p.
	Partition number (1-4, default 1): 
	First sector (2048-5242879, default 2048): 
	Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-5242879, default 5242879): +2G
	
	Created a new partition 1 of type 'Linux' and of size 2 GiB.
	
	Command (m for help): n
	Partition type
	   p   primary (1 primary, 0 extended, 3 free)
	   e   extended (container for logical partitions)
	Select (default p): p
	Partition number (2-4, default 2): 
	First sector (4196352-5242879, default 4196352): 
	Last sector, +/-sectors or +/-size{K,M,G,T,P} (4196352-5242879, default 5242879): 
	
	Created a new partition 2 of type 'Linux' and of size 511 MiB.
	
	Command (m for help): p
	Disk /dev/sda: 2.5 GiB, 2684354560 bytes, 5242880 sectors
	Disk model: Virtual disk    
	Units: sectors of 1 * 512 = 512 bytes
	Sector size (logical/physical): 512 bytes / 512 bytes
	I/O size (minimum/optimal): 512 bytes / 512 bytes
	Disklabel type: dos
	Disk identifier: 0x61e952fa
	
	Device     Boot   Start     End Sectors  Size Id Type
	/dev/sda1          2048 4196351 4194304    2G 83 Linux
	/dev/sda2       4196352 5242879 1046528  511M 83 Linux
	
	Command (m for help): w
	The partition table has been altered.
	Calling ioctl() to re-read partition table.
	Syncing disks.
``` 
5. ```bash
	root@k8s:~/devops-netology# sfdisk -d /dev/sda > ./fs/partitions-sda.txt
	root@k8s:~/devops-netology# sfdisk -d /dev/sdb < ./fs/partitions-sda.txt
   ```
6. `mdadm --create --verbose /dev/md0 -l 1 -n 2 /dev/sda1 /dev/sdb1`
7. `mdadm --create --verbose /dev/md1 -l 0 -n 2 /dev/sda2 /dev/sdb2`
8. ```bash
	vcreate /dev/md0 /dev/md1
	  Physical volume "/dev/md0" successfully created.
	  Physical volume "/dev/md1" successfully created.
	root@k8s:~/devops-netology# pvs
	  PV         VG        Fmt  Attr PSize    PFree   
	  /dev/md0             lvm2 ---    <2.00g   <2.00g
	  /dev/md1             lvm2 ---  1018.00m 1018.00m
	  /dev/sdc3  ubuntu-vg lvm2 a--   <79.00g  <39.50g
   ```
9. ```bash
	root@k8s:~/devops-netology# vgcreate vg01 /dev/md0 /dev/md1
	  Volume group "vg01" successfully created
	root@k8s:~/devops-netology# vgs
	  VG        #PV #LV #SN Attr   VSize   VFree  
	  ubuntu-vg   1   1   0 wz--n- <79.00g <39.50g
	  vg01        2   0   0 wz--n-  <2.99g  <2.99g
   ```
10. ```bash
	root@k8s:~/devops-netology# lvcreate -L 100M vg01 /dev/md1
	Logical volume "lvol0" created
    ```  
11. ` mkfs.ext4 /dev/vg01/lvol0 `
12. ```bash
	mkdir /tmp/new
	mount /dev/vg01/lvol0 /tmp/new
    ```
13. Выполнено  
```bash 
	root@k8s:~/devops-netology# ls -l /tmp/new
	total 22204
	drwx------ 2 root root    16384 Dec 11 18:07 lost+found
	-rw-r--r-- 1 root root 22719572 Dec 11 13:53 test.gz
```
14. ```bash
 	lsblk
	NAME                      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
	loop0                       7:0    0 55.5M  1 loop  /snap/core18/2253
	loop1                       7:1    0 55.5M  1 loop  /snap/core18/2246
	loop2                       7:2    0 10.3M  1 loop  /snap/kubectl/2120
	loop3                       7:3    0 61.8M  1 loop  /snap/core20/1242
	loop4                       7:4    0 61.9M  1 loop  /snap/core20/1270
	loop5                       7:5    0 10.4M  1 loop  /snap/kubectl/2177
	loop6                       7:6    0 73.1M  1 loop  /snap/lxd/21858
	loop7                       7:7    0 42.2M  1 loop  /snap/snapd/14066
	loop8                       7:8    0 73.1M  1 loop  /snap/lxd/21902
	loop9                       7:9    0 43.3M  1 loop  /snap/snapd/14295
	sda                         8:0    0  2.5G  0 disk  
	├─sda1                      8:1    0    2G  0 part  
	│ └─md0                     9:0    0    2G  0 raid1 
	└─sda2                      8:2    0  511M  0 part  
  	  └─md1                     9:1    0 1018M  0 raid0 
	    └─vg01-lvol0          253:1    0  100M  0 lvm   /tmp/new
	sdb                         8:16   0  2.5G  0 disk  
	├─sdb1                      8:17   0    2G  0 part  
	│ └─md0                     9:0    0    2G  0 raid1 
	└─sdb2                      8:18   0  511M  0 part  
  	  └─md1                     9:1    0 1018M  0 raid0 
	    └─vg01-lvol0          253:1    0  100M  0 lvm   /tmp/new
	sdc                         8:32   0   80G  0 disk  
	├─sdc1                      8:33   0    1M  0 part  
	├─sdc2                      8:34   0    1G  0 part  /boot
	└─sdc3                      8:35   0   79G  0 part  
  	  └─ubuntu--vg-ubuntu--lv 253:0    0 39.5G  0 lvm   /
	sr0                        11:0    1 1024M  0 rom   
    ```
15. ```bash
        root@k8s:~/devops-netology# gzip -t /tmp/new/test.gz
        root@k8s:~/devops-netology# echo $?
        0
    ```
16. `pvmove /dev/md1 /dev/md0`
17. `mdadm --fail /dev/md0 /dev/sda1`
18. ```
	 root@k8s:~/devops-netology# dmesg -T | tail -n 3
	[Sat Dec 11 18:08:28 2021] ext4 filesystem being mounted at /tmp/new supports timestamps until 2038 (0x7fffffff)
	[Sat Dec 11 18:21:23 2021] md/raid1:md0: Disk failure on sda1, disabling device.
        md/raid1:md0: Operation continuing on 1 devices.
    ```
19. ```bash
	root@k8s:~/devops-netology# gzip -t /tmp/new/test.gz
	root@k8s:~/devops-netology# echo $?
	0
     ```
20. Выполнено
