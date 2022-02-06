1. Выполнено. Данные импортированны из FireFox  
2. выполнено. В насройках указана двухфакторная авторизация через Google Authenticator
3. 
```bash
apt-get install apache2
a2enmod ssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
cat /etc/apache2/sites-available/test.conf
<VirtualHost *:443>
   ServerName 192.168.1.57
   DocumentRoot /var/www/

   SSLEngine on
   SSLCertificateFile /etc/ssl/certs/apache-selfsigned.crt
   SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key
</VirtualHost>
a2ensite test.conf
systemctl reload apache2
```
4. `nmap -script ssl-heartbleed,ssl-ccs-injection,ssl-dh-params -p 443 mail.ooo-nemo.ru` 
5. 
```bash
ssh-keygen
ssh-copy-id admin@192.168.1.60
ssh admin@192.168.1.60
```
6. 
```bash 
mv ~/.ssh/id_rsa ~/.ssh/test_rsa
cat ~/.ssh/config
Host test
User admin
HostName 192.168.1.60
Port 22
IdentityFile ~/.ssh/test_rsa
ssh test
```
7. `tcpdump -w mypcap.pcap -c 100`
