
def cypher_position_letter(letter, index_0, key):
    position = ord(letter) - index_0 + key # on ramene la lettre dans [0,25] en faisant -index_0
    position = (position % 26) + index_0 # ordre reel du caractere chiffre

    return position 

def main_position_letter(letter, index_0, key):
    position = ord(letter) - index_0 - key # on ramene la lettre dans [0,25] en faisant -index_0
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
            cypher_text.append(chr(position_caractere))
        else:
            position_caractere = cypher_position_letter(caractere, 97, cle)
            cypher_text.append(chr(position_caractere))

    cypher_text = "".join(cypher_text)
    return cypher_text

def cesar_decrypt(cypherText, cle):
    if not str(cle).isnumeric():
        print("la cle doit etre un entier")
        return
    
    cle = int(cle)
    if cle == 0:
        return cypherText 
    main_text = []
    for caractere in cypherText:
        if caractere == " ":
            main_text.append(caractere)
        elif caractere.isupper():
            position_caractere = main_position_letter(caractere, 65, cle)
            main_text.append(chr(position_caractere))
        else:
            position_caractere = main_position_letter(caractere, 97, cle)
            main_text.append(chr(position_caractere))
    
    main_text = "".join(main_text)

    return main_text
        

