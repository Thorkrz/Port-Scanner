from socket import * 
import threading
from rich.console import Console
console = Console() 
from datetime import datetime

name = input('Informe seu Nickname: ')

def logo(): 
      
      console.print ('''                             
    ____             __  _____                                 
   / __ \____  _____/ /_/ ___/_________ _____  ____  ___  _____
  / /_/ / __ \/ ___/ __/\__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 / ____/ /_/ / /  / /_ ___/ / /__/ /_/ / / / / / / /  __/ /    
/_/    \____/_/   \__//____/\___/\__,_/_/ /_/_/ /_/\___/_/     
                                                           
                                    [white]Coded By[/]: Thor_kryp                                        
''',style= "#AB14E1 bold") 

def bru(): 
  console.print(f"Hello, {name}!",style="on blue")
  host_name = gethostname()
  console.print("[red]Hostname:[/]",host_name,style="green") 
  ip =  gethostbyname(host_name)
  console.print("[red]IP:[/]",ip,style="green") 

     

def conScanner(tgtHost,tgtPorts):
   
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((tgtHost,tgtPorts))

        print (f'[*] {tgtPorts} TCP [Open] ' ) 
    except:
        print (f'[-] {tgtPorts} TCP [Closed] ' )
    finally:
        s.close()



def portScanner():
   target = input('Informe o IP/HOST Alvo: ')
   print('-' * 30)
   print(f"Scanning Alvo: {target}") 
   print("Scanning começou às: " + str(datetime.now()))
   print('-' * 30) 
   try:
        tgtIp = gethostbyname(target)
   except:
        print ('Unknown Host %s ' %target)
   try:
        tgtName = gethostbyaddr(tgtIp)
        print ('[*] Scan Results For: ' + tgtName[0])
   except:
         print ('[*] Scan Results for: ' + tgtIp)
   setdefaulttimeout(1)

   for port in range(650):
        t = threading.Thread(target=conScanner, args=(target,int(port)))
        t.start()


   

if __name__ == "__main__":
   logo()
   bru()
   portScanner() 

 

 
 
