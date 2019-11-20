from socket import *
import datetime
from threading import Thread
import time
udp_ip_address_r1 = '10.10.1.1'
send_port_no_r1 = 12002

udp_ip_address_r2 = '10.10.2.2'
send_port_no_r2 = 13032


udp_ip_address_s = '10.10.3.1'
send_port_no_s = 13062

udp_ip_address_s_to_r3 = '10.10.3.2'
udp_port_no_s_to_r3 = 14002


RTTfor_s_r3 = 0

PACKET_SIZE = 128

def server(ip, port, name):
	data_receiver = socket(AF_INET,SOCK_DGRAM)
	data_receiver.bind((ip,port))
	try:
		while True:
			data_receiver.settimeout(10)
			data,addr = data_receiver.recvfrom(PACKET_SIZE)
			data_receiver.settimeout(None)
			data_receiver.sendto(data,addr)
	except timeout:
		data_receiver.close()		

		
def main():
	r1 = Thread(target = server,args = (udp_ip_address_r1, send_port_no_r1, "r1"))
	r2 = Thread(target = server,args = (udp_ip_address_r2, send_port_no_r2, "r2"))
	r3 = Thread(target = server,args = (udp_ip_address_s, send_port_no_s, "r3"))
	

	r1.start()
	r2.start()
	r3.start()

	r1.join()
	r2.join()
	r3.join()
	

if __name__ == '__main__':
	main()

