import dns.resolver
import socket


def NS_record(x):
    try :       
        result = dns.resolver.resolve(x , 'NS')

        for val in result :
            print(f'NS Record : {val.to_text()}')
    except dns.resolver.NXDOMAIN:
        print(": The queried domain name does not exist.")
    except dns.resolver.NoAnswer: 
        print("The domain exists, but has no record of the requested type or class.")
    except Exception as e:
        print(f"  A Record: Error - {e}")

def SOA_record(domain):
    try :       
        result = dns.resolver.resolve(domain , 'SOA')

        for val in result :
            print(f'SOA Record : {val.to_text()}')
    except dns.resolver.NXDOMAIN:
        print(": The queried domain name does not exist.")
    except dns.resolver.NoAnswer: 
        print("The domain exists, but has no record of the requested type or class.")
    except Exception as e:
        print(f"  A Record: Error - {e}")

def A_record(domain):
    try :       
        result = dns.resolver.resolve(domain , 'A')

        for val in result :
            print(f'A Record : {val.to_text()}')
    except dns.resolver.NXDOMAIN:
        print(": The queried domain name does not exist.")
    except dns.resolver.NoAnswer: 
        print("The domain exists, but has no record of the requested type or class.")
    except Exception as e:
        print(f"  A Record: Error - {e}")

def AAAA_record(domain):
    try :       
        result = dns.resolver.resolve(domain , 'AAAA')

        for val in result :
            print(f'SOA Record : {val.to_text()}')
    except dns.resolver.NXDOMAIN:
        print(": The queried domain name does not exist.")
    except dns.resolver.NoAnswer: 
        print("The domain exists, but has no record of the requested type or class.")
    except Exception as e:
        print(f"  A Record: Error - {e}")

def reverse(ip):
    try:
        hostname, _ = socket.getnameinfo((ip, 0), 0)
        print(f"Hostname: {hostname}")
    except socket.herror:
        print("Unknown host")


choice = input("resolve (1) or inverse (2): ")

if choice == "1":
    domain = input("enter a domain: ")
    NS_record(domain)
    AAAA_record(domain)
    A_record(domain)
    SOA_record(domain)


elif choice == "2" :
    ip = input ("enter an ip: ")
    reverse(ip)

else :
    print ("please enter 1 or 2")
    
    

    


