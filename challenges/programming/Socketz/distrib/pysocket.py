#!/usr/bin/env python3 

import socket 

def main(): 
	try: 
		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		clientsocket.connect(('127.0.0.1',12345)) # Connect to ip address and port 
		clientsocket.sendall(input().encode()) # Write string 
		print(clientsocket.recv(4096).decode()) # Read string 
		clientsocket.close() 
	except socket.error as e: print(str(e))

if __name__ == "__main__": 
	main() 
