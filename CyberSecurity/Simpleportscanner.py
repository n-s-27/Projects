#A shitty version of NMAP (port scanner) to use through Devtools 

import sys #to use cli args and etc
import socket
from datetime import datetime

#define the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4

else:
    print("Error: invalid amount of arguments.")
    print("Reminder, Syntax is : python3 scanner.py <ip>")
    
#Make a banner
print("-" * 50)
print("Scanning target:" + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is ipv4, SOCK_STREAM is the port
        socket.setdefaulttimeout(1) # timeout is a float
        result = s.connect_ex((target, port)) #returns error indicator if error on connection, else will return 0
        print("Checking port {}".format(port))   #lets us know if we are actually checking
        if result == 0: 
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program...")
    sys.exit()

except socket.gaierror: 
    print("\nHostname could not be found.")
    sys.exit()

except socket.error:
    print("\nCouldn't connect to server.")
    sys.exit()



#things to add:
    # *threading to be more efficient bc allows multi-processing 
    #