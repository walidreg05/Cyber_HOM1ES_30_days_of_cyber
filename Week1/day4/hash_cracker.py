import hashlib
import sys
import pyfiglet
from hashid import HashID

ascii_banner = pyfiglet.figlet_format("H e l l o   H O M 1 E S")
print(ascii_banner)

def hash_identifier():
    identifier = HashID()
    target_hash= input("please enter a hash: ")
    results = identifier.identifyHash(target_hash)
    print(results)
    for result in results:
        print (f"possible Hash type : {result.name}")
""" 
option2:
if len(hash) == 32: return "MD5"
    elif len(hash) == 40: return "SHA1"
    elif len(hash) == 56: return "SHA224"
    elif len(hash) == 64: return "SHA256"
    elif len(hash) == 96: return "SHA384"
    elif len(hash) == 128: return "SHA512"
"""

def hash_cracker():
    print ("Available possibilities: MD5 -- SHA1 -- SHA224 -- SHA512 -- SHA384 -- SHA256--")
    wordlist_location = input("enter the wordlist location: ")
    hash_type =  input("enter the hash_type (please respect the syntax mentionned before): ")
    hash = input("enter a hash: ")
    try:
    
        with open(wordlist_location, "r", errors="ignore") as file:
            
            # MODIFICATION 2: Added a loop to check one word at a time
            for line in file:         
                word = line.strip() # remove the \n 
                
                if hash_type == "MD5":
                    hash_object = hashlib.md5(f"{word}".encode("utf-8")) 
                    hashed = hash_object.hexdigest() 
                    if hash == hashed:
                        print (f"hash value founded:{word} ")
                        break 
                        
                elif hash_type == "SHA1":
                    hash_object = hashlib.sha1(f"{word}".encode("utf-8")) 
                    hashed = hash_object.hexdigest() 
                    if hash == hashed:
                        print (f"hash value founded:{word} ")
                        break
                        
                elif hash_type == "SHA512":
                    hash_object = hashlib.sha512(f"{word}".encode("utf-8")) 
                    hashed = hash_object.hexdigest() 
                    if hash == hashed:
                        print (f"hash value founded:{word} ")
                        break
                        
                elif hash_type == "SHA224":
                    hash_object = hashlib.sha224(f"{word}".encode("utf-8")) 
                    hashed = hash_object.hexdigest() 
                    if hash == hashed:
                        print (f"hash value founded:{word} ")
                        break
                        
                elif hash_type == "SHA384":
                    hash_object = hashlib.sha384(f"{word}".encode("utf-8")) 
                    hashed = hash_object.hexdigest() 
                    if hash == hashed:
                        print (f"hash value founded:{word} ")
                        break
                        
                elif hash_type == "SHA256":
                    hash_object = hashlib.sha256(f"{word}".encode("utf-8")) 
                    hashed = hash_object.hexdigest() 
                    if hash == hashed:
                        print (f"hash value founded:{word} ")
                        break
                else: 
                    print("please enter a valid hash type")
    except FileNotFoundError:
        print(" wordlist file not found , check the path and try again.")


print("-----What dou you want to doo ??-----")
print("-----crack (1) or identify(2)-----")
choice = input("enter a value: ")
if choice == "1":
     hash_cracker()
elif choice == "2":
     hash_identifier()
else :
     print("please enter 1 or 2:")

     


        
         

        



