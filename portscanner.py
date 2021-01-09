#!/usr/bin/python
import socket
target = input('[*] Enter Target IP: ') #taget input for ip address you wish to scan

while True:
    port_min = int(input('[*] Enter port to start scanning from: '))
    port_max = int(input('{*] Enter port to scan too: '))
    if port_min <= port_max: #ensuring that min port is less than max port
        break
    
print ('scanning',target, 'from port',port_min,' to',port_max,' please wait..') #some user friendly conformation that scan has began

for port in range(port_min, port_max + 1): #ports in range of min and max ports and +1 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defining what internet protocole to use with what module AF_INET is for ip address and domain names.
    if not sock.connect_ex((target, port)):
        print('[*] Port', port, '/tcp','is open')
    sock.close()
       
