import socket
HOST = input ("ENTER UR TARGET")
try:
    for port in range (20 , 1025):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.5)
        #testing theconnection 
        result = s.connect_ex((HOST , port)) #result = 0 --> port open 
        if result == 0 :
            print (f"Port {port} is open ")
except KeyboardInterrupt:
    print("\nprogram interrupted by user.")
    sys.exit()
except socket.error: 
    print("\nServer unreacheable ")
    sys.exit()
except socket.gaierror:
    print("\n cannot resolve the host name") 
    sys.exit()
