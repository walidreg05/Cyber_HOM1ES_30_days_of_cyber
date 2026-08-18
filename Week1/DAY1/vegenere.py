# key ="ABC"
key_v = input('please enter a key value: ')
key= key_v.upper()

transf_message =''
def vegenere_cypher (text):
    new = ''
    text = text.upper()
    for i in range (len(text)):
        
        x = text[i]
        y = key[i%(len(key))]
        x_val = ord(x) - ord('A')
        y_val = ord(y) - ord('A')     
        new += chr((x_val + y_val) % 26 + ord('A'))
        
    return new

print(vegenere_cypher("GAZAA"))      

