#! /bin/sh

echo 'hello'

apt-get update && apt-get install -y \
         openssh-server \
         nano \
         vsftpd

sed -i '/PasswordAuthentication yes/s/^#//g' /etc/ssh/sshd_config

useradd -ms /bin/bash bridger 
yes bridger | passwd bridger
useradd -ms /bin/bash jim
yes amanda | passwd jim

python3 /app/apsembb/manage.py migrate

systemctl enable ssh

