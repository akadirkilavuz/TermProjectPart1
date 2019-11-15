import random
from socket import *
import datetime
import time
from threading import Thread



udp_ip_address_s = '10.10.1.1'
udp_port_no_s = 12002

udp_ip_address_r2 = '10.10.8.2'
udp_port_no_r2 = 12022

udp_ip_address_d = '10.10.4.2'
udp_port_no_d = 12052

PACKET_SIZE = 128


epoch = datetime.datetime.utcfromtimestamp(0)

def time_millis(dt):
    return int((dt - epoch).total_seconds() * 1000.0)

RTTfor_R1_s = 0
RTTfor_R1_R2 = 0
RTTfor_R1_d = 0

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
				global RTTfor_R1_s
				RTTfor_R1_s += elapsed
				print(f'{data} {messages} {elapsed}')
			except timeout:
				print('REQUEST TIME OUT')

	if(name=="r2"):		
		for messages in range(10):		
			data_send = socket(AF_INET,SOCK_DGRAM)
			data_send.settimeout(0.5)
			message = b'test'
			start = time.time()
			data_send.sendto(message,(udp_ip_address_r2,udp_port_no_r2))
			try:
				data,addr = data_send.recvfrom(PACKET_SIZE)
				end = time.time()
				elapsed = end - start
				global RTTfor_R1_R2
				RTTfor_R1_R2 = RTTfor_R1_R2 + elapsed
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
				global RTTfor_R1_d
				RTTfor_R1_d += elapsed
				print(f'{data} {messages} {elapsed}')
			except timeout:
				print('REQUEST TIME OUT')


def main():
	s = Thread(target = client,args = (udp_ip_address_s, udp_port_no_s, "s"))
	R2 = Thread(target = client,args = (udp_ip_address_r2, udp_port_no_r2, "r2"))
	d = Thread(target = client,args = (udp_ip_address_d, udp_port_no_d, "d"))
	
	s.start()
	R2.start()
	d.start()

	s.join()
	R2.join()
	d.join()

	print(RTTfor_R1_s/1000.0)
	print(RTTfor_R1_R2/1000.0)
	print(RTTfor_R1_d/1000.0)

if __name__ == '__main__':
	main()

