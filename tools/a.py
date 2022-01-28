#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from urllib2 import Request, urlopen, URLError, HTTPError
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    elif os.name == 'mac':
        _ = os.system('clear')
    elif os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('clear')
def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1

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

       \033[93m Git-Hub: https://github.com/not-body/  \033[94m\033[1m    V 1.4                                                                                                         
                     
                                                  """
clear()
print(ressamnotbody)

f = open("tools/link.txt","r")
link = raw_input("\033[92m Site Adı Girin (ex : example.com ve ya www.example.com ): ")
print "\n\n\033[93mBulunan Linkler : \033[95m\n"
while True:
	sub_link = f.readline()
	if not sub_link:
		break
	req_link = "http://"+link+"/"+sub_link
	req = Request(req_link)
	try:
		response = urlopen(req)
	except HTTPError as e:
		continue
	except URLError as e:
		continue
	else:
		print "OK => ",req_link
        
exit()