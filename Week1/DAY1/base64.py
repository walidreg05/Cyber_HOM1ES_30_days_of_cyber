alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" 
#1st step , convert to binary representation 
def base64_encoder(text) :
    index = 0
    bin_val = ''
    final_b64 = ''
    bytes_val = text.encode('utf-8')
    for L in text :
        x = int(ord(L))    
        bin_val+= str(f"{x:08b}") # it convert every integer value to the 8bit binary representation
#2nd step separat binaries into groups of 6 bits 
    test = len((bin_val))%6

    zero_nedded = (6 - test) %6
    print(zero_nedded)
    bin_val += "0" * zero_nedded
    print(bin_val)
    cord = (len(bin_val)/6)
    print (cord)
    new = ''
    while index < len(bin_val):
        new += bin_val[index :index+6] + " "
        index += 6
        
    #now splitung the values
    for group in new.split():
        decimal_val = int(group, 2)         
        final_b64 += alphabet[decimal_val]

    remainder = len(text) % 3

    if remainder == 1:
        final_b64 += "=="
    elif remainder == 2:
        final_b64 += "="

    print("Final encoded HOM13S:")
    print(final_b64)




