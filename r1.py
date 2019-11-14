import random
from socket import *
import datetime
import time
from threading import Thread

udp_ip_address_s = '10.10.1.1'
udp_port_no_s = 12002

udp_ip_address_r2 = '10.10.8.1'
udp_port_no_r2 = 12022

udp_ip_address_d = '10.10.4.1'
udp_port_no_d = 12052

PACKET_SIZE = 128

epoch = datetime.datetime.utcfromtimestamp(0)

def time_millis(dt):
    return int((dt - epoch).total_seconds() * 1000.0)



def client(ip, port, name):
	if(name=="s"):	
		for messages in range(1000):		
			data_send = socket(AF_INET,SOCK_DGRAM)
			data_send.settimeout(30)
			message = b'test'
			start = time.time()
			data_send.sendto(message,(udp_ip_address_s,udp_port_no_s))
			try:
				while True:
					data,addr = data_send.recvfrom(PACKET_SIZE)
					end = time.time()
					elapsed = end - start
					print(f'{data} {messages} {elapsed}')
			except timeout:
				print('REQUEST TIME OUT')

	if(name=="r2"):		
		for messages in range(1000):		
			data_send = socket(AF_INET,SOCK_DGRAM)
			data_send.settimeout(30)
			message = b'test'
			start = time.time()
			data_send.sendto(message,(udp_ip_address_r2,udp_port_no_r2))
			try:
				while True:
					data,addr = data_send.recvfrom(PACKET_SIZE)
					end = time.time()
					elapsed = end - start
					print(f'{data} {messages} {elapsed}')
			except timeout:
				print('REQUEST TIME OUT')

	if(name=="d"):		
		for messages in range(1000):		
			data_send = socket(AF_INET,SOCK_DGRAM)
			data_send.settimeout(30)
			message = b'test'
			start = time.time()
			data_send.sendto(message,(udp_ip_address_d,udp_port_no_d))
			try:
				while True:
					data,addr = data_send.recvfrom(PACKET_SIZE)
					end = time.time()
					elapsed = end - start
					print(f'{data} {messages} {elapsed}')
			except timeout:
				print('REQUEST TIME OUT')


def main():
	s = Thread(target = client,args = (udp_ip_address_s, udp_port_no_r1, "s"))
	#R2 = Thread(target = client,args = (udp_ip_address_r2, udp_port_no_r2, "r2"))
	d = Thread(target = client,args = (udp_ip_address_d, udp_port_no_d, "d"))
	
	s.start()
	#R2.start()
	d.start()

	s.join()
	#R2.join()
	d.join()

if __name__ == '__main__':
	main()

