from cesar import *
from vigenere import *


texte = "Bonjour mon ami"

# *********************    chiffrement de cesar ******************************
print("\n*********************    chiffrement de cesar ******************************")
cypher_text = cesar_encrypt(texte,5)
print(cypher_text)

main_text = cesar_decrypt(cypher_text,5)
print(main_text)

# *********************    chiffrement de vigenere ******************************
print("\n*********************    chiffrement de vigenere ******************************")
cypher_text = vigenere(texte,"bc")
print(cypher_text)

main_text = vigenere_decrypt(cypher_text, "bc")
print(main_text)

mon_fichier = open("texte.txt", "r")
content = mon_fichier.read()
mon_fichier.close()

cypher_content = cesar_encrypt(content, 21)


newF = open("new.txt", "a")
newF.write(cypher_content)
newF.close()