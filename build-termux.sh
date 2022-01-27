#! /bin/bash 
echo BU Dosyayı Sadece Metasploit-Framework Kurulu Değilse Açın Dosya 10 Saniye Sonra Otomatik Olarak Kurulumlara Başlayacaktır!!!

sleep 10

cd $HOME
pkg update && pkg upgrade -y &&pkg install postgresql && pkg install openssh wget curl git -y && wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh && chmod +x  metasploit.sh && ./metasploit.sh
