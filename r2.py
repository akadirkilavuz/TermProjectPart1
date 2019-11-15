import random
from socket import *
import datetime
import time
from threading import Thread



udp_ip_address_s = '10.10.2.2'
udp_port_no_s = 13032

udp_ip_address_d = '10.10.5.2'
udp_port_no_d = 12082

udp_ip_address_R1 = '10.10.8.2'
udp_port_no_R1 = 12022

udp_ip_address_R3 = '10.10.6.1'
udp_port_no_R3 = 14000

PACKET_SIZE = 128


epoch = datetime.datetime.utcfromtimestamp(0)

def time_millis(dt):
    return int((dt - epoch).total_seconds() * 1000.0)

RTTfor_R2_s = 0
RTTfor_R2_d = 0


def server(ip, port, name):
    data_receiver = socket(AF_INET,SOCK_DGRAM)
    data_receiver.bind((ip,port))
    try:
        while True:
            data_receiver.settimeout(30)
            data,addr = data_receiver.recvfrom(PACKET_SIZE)
            data_receiver.settimeout(None)
            data_receiver.sendto(data,addr)
    except timeout:
        data_receiver.close()

def client(ip, port, name):
    if(name=="s"):  
        for messages in range(1000):      
            data_send = socket(AF_INET,SOCK_DGRAM)
            data_send.settimeout(0.5)
            message = b'test'
            start = time.time()
            data_send.sendto(message,(udp_ip_address_s,udp_port_no_s))
            try:
                data,addr = data_send.recvfrom(PACKET_SIZE)
                end = time.time()
                elapsed = end - start
                global RTTfor_R2_s
                RTTfor_R2_s += elapsed
                print(f'{data} {messages} {elapsed}')
            except timeout:
                print('REQUEST TIME OUT')

    if(name=="d"):      
        for messages in range(1000):      
            data_send = socket(AF_INET,SOCK_DGRAM)
            data_send.settimeout(0.5)
            message = b'test'
            start = time.time()
            data_send.sendto(message,(udp_ip_address_d,udp_port_no_d))
            try:
                data,addr = data_send.recvfrom(PACKET_SIZE)
                end = time.time()
                elapsed = end - start
                global RTTfor_R2_d
                RTTfor_R2_d += elapsed
                print(f'{data} {messages} {elapsed}')
            except timeout:
                print('REQUEST TIME OUT')


def main():

    listen_r1 = Thread(target = server,args = (udp_ip_address_R1, udp_port_no_R1, "r1"))
    listen_r3 = Thread(target = server,args = (udp_ip_address_R3, udp_port_no_R3, "r3"))

    listen_r1.start()
    listen_r3.start()

    

    s = Thread(target = client,args = (udp_ip_address_s, udp_port_no_s, "s"))
    d = Thread(target = client,args = (udp_ip_address_d, udp_port_no_d, "d"))
    
    s.start()
    d.start()

    listen_r1.join()
    listen_r3.join()

    s.join()
    d.join()

    print(RTTfor_R2_s/1000.0)
    print(RTTfor_R2_d/1000.0)

if __name__ == '__main__':
    main()


