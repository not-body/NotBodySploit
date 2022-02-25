#! /bin/bash 
apt-get -y install php openssh git wget
a= read -p "Metasploit-Framework Kurulsun Mu [Y/N]: "
if [[ a == "y" || a == "Y" || a == "Yes" || a == "yes" || "YES" ]]; then
cd $HOME
pkg update && pkg upgrade -y &&pkg install postgresql && pkg install openssh wget curl git -y && wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh && chmod +x  metasploit.sh && ./metasploit.sh
fi
cd /data/data/com.termux/files/usr/share
git clone https://github.com/not-body/NotBodySploit
cd /data/data/com.termux/files/usr/bin
echo python3 /data/data/com.termux/files/usr/share/NotBodySploit/notbody-termux.py > notbody
chmod +x notbody
echo Kurulum Tamamlandı
