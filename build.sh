#! /bin/bash
apt-get -y install php openssh git wget
apt install xtitle
cd /usr/share
git clone https://github.com/not-body/NotBodySploit
cd /bin
echo python3 /usr/share/NotBodySploit/notbody.py > notbody

echo Kurulum Tamamlandı
