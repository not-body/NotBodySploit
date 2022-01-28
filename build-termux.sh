#! /bin/bash 
apt-get -y install php openssh git wget
a= read -p "Metasploit-Framework Kurulu Mu [Y/N]: "
if [[ a == "y" || a == "Y" || a == "Yes" || a == "yes" || "YES" ]]; then
cd $HOME
pkg update && pkg upgrade -y &&pkg install postgresql && pkg install openssh wget curl git -y && wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh && chmod +x  metasploit.sh && ./metasploit.sh
echo Kurulum Tamamlandı :D
else
echo Kurulum Tamamlandı :D
fi