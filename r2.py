import random
from socket import *
import datetime
from threading import Thread

udp_ip_address_s = '10.10.1.1'
udp_port_no_r1 = 12002

udp_ip_address_r2 = '10.10.8.1'
udp_port_no_r2 = 12022

send_ip_address_r2 = '10.10.8.1'
send_port_no_r2 = 12022

send_ip_address_d = '10.10.4.2'
send_port_no_d = 12052

PACKET_SIZE = 128

epoch = datetime.datetime.utcfromtimestamp(0)

def time_millis(dt):
    return int((dt - epoch).total_seconds() * 1000.0)


def server(ip, port, name):
	data_receiver = socket(AF_INET,SOCK_DGRAM)
	data_receiver.bind((ip,port))
	try:
		while True:
			data_receiver.settimeout(30)
			data,addr = data_receiver.recvfrom(PACKET_SIZE)
			data_receiver.settimeout(None)
			if(name == "r2" and data and data != ''):
				data_receiver.sendto(data, (send_ip_address_d,send_port_no_d))
			
def main():
	s = Thread(target = server,args = (udp_ip_address_s, udp_port_no_r1, "s"))
	R2 = Thread(target = server,args = (udp_ip_address_r2, udp_port_no_r2, "r2"))
	
	s.start()
	R2.start()

	s.join()
	R2.join()

if __name__ == '__main__':
	main()

