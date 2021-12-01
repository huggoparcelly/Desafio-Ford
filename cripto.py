import binascii

vin = input("Digite o vin: ")

deslocamento = 3

letras = [
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
  "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Palavra criptografia nivel 1
cripto_nivel1 = ""

# veriricando cada caracter e retornando o caracter com deslocamento
for char in vin:
    if char in letras:
        posicao_char = letras.index(char)
        nova_posicao = posicao_char + deslocamento
        # captura o caracter com o deslocamento
        if nova_posicao >= len(letras):
            nova_posicao -= len(letras)
        cripto_nivel1 += letras[nova_posicao]

    if char in numeros:
        posicao_char = numeros.index(char)
        nova_posicao = posicao_char + deslocamento
        if nova_posicao >= len(numeros):
            nova_posicao -= len(numeros)
        cripto_nivel1 += numeros[nova_posicao]


cripto_hexa = binascii.hexlify(bytes(cripto_nivel1, "utf-8"))


print(cripto_hexa)