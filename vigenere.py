from cesar import cypher_position_letter, cesar_encrypt

def decouper(texte, taille_morceau):
    new_text = []
    for caractere in texte:
        new_text.append(caractere)

    if taille_morceau == 1:
        print(new_text)
        return new_text
    
    to_encrypt = []
    word = []
    for i in range(len(new_text)):
        if len(word) == taille_morceau:
            to_encrypt.append("".join(word))
            word = []
        word.append(new_text[i])
    
    if len(word) != 0:
        to_encrypt.append("".join(word))
     
    return to_encrypt

def vigenere(texte,cle):
    # La cle ici est un mot quelconque comportant des lettres

    cle = cle.lower()  # la cle ne doit etre qu'en minuscule
    l = len(cle) # la longueur de la cle
    key = []
    
    new_text = decouper(texte, l)
    
    for caractere in cle:
        position_caractere = ord(caractere) -97
        key.append(position_caractere)
    
    if l == 1:  # on se ramene au simple chiffrement de cesar
        cypher_text = cesar_encrypt(texte, key[0])
        return cypher_text
    
    cypher_text = []
    for i in range(len(new_text)):
        word = new_text[i]
        cypher_word = []
        for j in range(len(word)):
            if word[j] == " ":
                cypher_word.append(word[j])
            else:
                cypher_word.append(cesar_encrypt(word[j],key[j]))
        
        cypher_word = "".join(cypher_word)
        
        cypher_text.append(cypher_word)
    
    cypher_text = "".join(cypher_text)

    return cypher_text

texte = "Bonjour mon ami"
#decouper(texte,2)
cypher_text = vigenere(texte,"bc")
print(cypher_text)