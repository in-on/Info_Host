#!/bin/python
import socket 
import sys
print("\n ",len(socket.gethostname()) * "*")
print (f"Hi Mr.{socket.gethostname()}  \n")

# info system Hostname ipv4
def info():
 print("[*] Hostname :",socket.gethostname() )
 print("[*] IP Address IPv4 : ",socket.gethostbyname(socket.gethostname()) ,"\n")


# info everythink input host_name
def info2():
 Host_name=sys.argv[2]
 info = socket.gethostbyname_ex(Host_name)
 print(f"[*] Hostname :{info[0]} \n")

 print (f"[*] Aliases : {len(info[1])} \n")
 for alias in info [1]:
   print(alias)

 print(f"[*] IP Address : {len(info[2])} ")
 for address in info[2]:
   print(address)


# info everythink input ip_address
def info3():
 address=sys.argv[2]
 info = socket.gethostbyaddr(address)
 print(f"[*] Hostname :{info[0]} \n")

 print (f"[*] Aliases : {len(info[1])} \n")
 for alias in info [1]:
   print(alias,"\n")

 print(f"[*] IP Address : {len(info[2])} \n ")
 for address in info[2]:
   print(address)

if len(sys.argv) < 2:
    print("[*] Usage: python info_host.py <1 info system|2 Host|3 addres|0 exit >")
    print ("Example ./info_host.py 1 ")
    print ("Example ./info_host.py 2 www.google.com ")
    print ("Example ./info_host.py 3 8.8.8.8 ")
    sys.exit()

choice = sys.argv[1]

match choice:
    case "1":
       info()
    case "2":
        info2()
    case "3":
        info3()
    case "0":
        print("Goodbye!")
    case _:
        print("Not Answer")
