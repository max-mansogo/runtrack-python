
def cesar(message, desplazamiento):
    message_ciffré = ""
    for lettre in message:
        if lettre.isalpha():
            if lettre.isupper():
                indice = ord(lettre) - ord('A')
                lettre_ciffrée = chr((indice + desplazamiento) % 26 + ord('A'))
            else:
                indice = ord(lettre) - ord('a')
                lettre_ciffrée = chr((indice + desplazamiento) % 26 + ord('a'))
            message_ciffré += lettre_ciffrée
        else:
            message_ciffré += lettre
    return message_ciffré

message_original = "Hello, world!"
desplazamiento = 3

mensaje_cifrado = cesar(message_original, desplazamiento)
print(mensaje_cifrado)  
