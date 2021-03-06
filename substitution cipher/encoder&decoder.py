import string
import codecs 


with codecs.open('alph.txt',encoding='utf-8') as f: # utf-8 not necessary that's special for russian language
    alph = f.read()
alph = alph + alph.upper()
print(alph)
with codecs.open('key.txt',encoding='utf-8') as f:
    key = f.read()
key = key + key.upper()
print(key)
#alph and key must be equal lenght
with codecs.open('text.txt',encoding='utf-8') as f:
    text = f.read()

print('1 - Encode')
print('2 - Decode')
k = input()
if k == '1':
    enc = str.maketrans(alph,key)#save in enc compare alph string and key string
    
    encodedtext = text.translate(enc) # makes bijective substitution
    print(encodedtext)
    with codecs.open('res.txt',"w",encoding='utf-8') as f:
        f.write(encodedtext)
elif k == '2':
    dec = str.maketrans(key,alph)
    decodedtext = text.translate(dec)
    print(decodedtext)
    with open('res.txt',"w") as f:
        f.write(decodedtext)
        
else:
    print('Wrong operation')
