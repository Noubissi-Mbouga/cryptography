
def cypher_position_letter(letter, index_0, key):
    position = ord(letter) - index_0 + key # on ramene la lettre dans [0,25]
    position = (position % 26) + index_0 # ordre reel du caractere chiffre

    return position 

def cesar_encrypt(texte, cle):
    # texte est le texte a chiffrer
    # cle ici represente le pas de decalage. c'est un entier

    if not str(cle).isnumeric():
        print("la cle doit etre un entier")
        return
    
    cle = int(cle)
    if cle == 0:
        return texte
    
    cypher_text = []

    for caractere in texte:
        if caractere == " ":
            cypher_text.append(" ")
        elif caractere.isupper():
            position_caractere = cypher_position_letter(caractere, 65, cle)
        else:
            position_caractere = cypher_position_letter(caractere, 97, cle)

        cypher_text.append(chr(position_caractere))
    cypher_text = "".join(cypher_text)
    return cypher_text



texte = "Bonjour mon ami"
new = cesar_encrypt(texte,5)
print(new)