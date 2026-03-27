def xor_cypher(main_file, cypher_file,key):
    key_bytes = key.encode()
    l = len(key_bytes)
    mf = open(main_file,"rb")
    cf = open(cypher_file,"wb")

    i=0

    while True:
        chunck = mf.read(4096)

        if not chunck:
            break
        chiffre = bytearray()
        for byte in chunck:
            chiffre.append(byte ^ key_bytes[i % l])
            i+=1

        cf.write(chiffre)

    mf.close()
    cf.close()

def xor_decrypt(cypher_file, new_file,key):
    key_bytes = key.encode()
    l = len(key_bytes)
    cf = open(cypher_file, 'rb')
    
    if new_file.endswith(".txt"):
        nf = open(new_file, 'w')
    else:
        nf = open(new_file, 'wb')

    i=0

    while True:
        chunck = cf.read(4096)

        if not chunck:
            break

        caractere = bytearray()
        
        for byte in chunck:
            caractere.append(byte ^ key_bytes[i % l])    
            i+=1
        if new_file.endswith(".txt"):
            nf.write(caractere.decode())
        else:
            nf.write(caractere)


xor_decrypt("code1.enc","code.png", "morning")
        