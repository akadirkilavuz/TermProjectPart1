import random
from socket import *
import datetime
from threading import Thread

udp_ip_address_r1 = '10.10.4.1'
send_port_no_r1 = 12052

udp_ip_address_r2 = '10.10.5.1'
send_port_no_r2 = 12082

udp_ip_address_r3 = '10.10.7.1'
send_port_no_r3 = 13002


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
			data_receiver.sendto(data,addr)
	except timeout:
		print ("{} UDP connection will be closed").format(name)
		data_receiver.close()
		
def main():
	r1 = Thread(target = server,args = (udp_ip_address_r1, send_port_no_r1, "r1"))
	r2 = Thread(target = server,args = (udp_ip_address_r2, send_port_no_r2, "r2"))
	r3 = Thread(target = server,args = (udp_ip_address_r3, send_port_no_r3, "r3"))

	r1.start()
	r2.start()
	r3.start()

	r1.join()
	r2.join()
	r3.join()

if __name__ == '__main__':
	main()

