import webview
import winreg
import time
import json
import requests
import logging
from requests.auth import HTTPBasicAuth
import os
from playsound import playsound  




logging.captureWarnings(True)
string = r'SOFTWARE\WOW6432Node\Tencent\LOL'
handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, string, 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_READ))
location, _type = winreg.QueryValueEx(handle, "InstallPath")#获取lol地址
lockfilepath = location +'\\LeagueClient\\lockfile'#获取lol地址地址

        
with open(lockfilepath) as lines:

                for line in lines:
                    port=(line.split(":" ) [2] )    
                    key= (line.split(":" ) [3] ) #读取端口和key
                    path= 'https://127.0.0.1:'+ port+'/lol-summoner/v1/current-summoner/'  
                    user ='riot'
                    password=key
                    r = requests.get(path, auth=HTTPBasicAuth(user, password),verify=False)           
                    re = json.loads(r.text)# 转化      
                    ttk= re["internalName"] #读取标题
                    print(ttk)
                    kill1=1
                    while kill1<1000:
                        path2 ="https://127.0.0.1:2999/liveclientdata/playerscores?summonerName="+ttk          
                        r = requests.get(path2,verify=False)
                        om= json.loads(r.text)# 转化      
                        kill1= om["kills"] #读取标题
                        assists1= om["assists"] #读取标题
                        death1= om["deaths"] #读取标题
                            
                        time.sleep(2)
                        path2 ="https://127.0.0.1:2999/liveclientdata/playerscores?summonerName="+ttk          
                        r = requests.get(path2,verify=False)
                        om= json.loads(r.text)# 转化      
                        kill2= om["kills"] #读取标题
                        assists2= om["assists"] #读取标题
                        death2= om["deaths"] #读取标题
                        if kill2>kill1:
                                playsound('1.mp3') 
                        if assists2>assists1:                   
                                playsound('2.mp3') 
                        if  death2>death1: 
                                playsound('3.mp3') 
                

        
        
