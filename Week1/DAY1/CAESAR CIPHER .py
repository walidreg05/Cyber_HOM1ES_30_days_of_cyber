#!/usr/bin/env python3
message_2_enc = input ("Enter ut text here homiie: ")
new = ""
shift = 10
for L in message_2_enc :
    if L.isupper():
        new += chr((ord(L) -65 +shift )%26 + 65 )
    elif L.islower():
        new += chr((ord(L) - 97 + shift )%26 + 97)
    else :
        new += L 

print("ur result is :")
print(new)