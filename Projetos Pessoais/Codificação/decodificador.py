codigo = input("Insira a frase codificada: ")

#Listas dos códigos
codigomaiusculas = "nijklmtuvwxyzabcdopqrsefgh*"
codigominusculas = "ZAJKLMNOPQRSTUVWXYBCDEFGHI"
codigonumeros = "5678920134"

#Listas dos símbolos possíveis
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
minusculas = maiusculas.lower()
numeros = "0123456789"

frase_original = ""
for c in codigo:
    if (c not in codigomaiusculas) and (c not in codigominusculas) and (c not in codigonumeros):
        frase_original += c
    elif c in codigomaiusculas:
        frase_original += maiusculas[codigomaiusculas.index(c)]
    elif c in codigominusculas:
        frase_original += minusculas[codigominusculas.index(c)]
    elif c in codigonumeros:
        frase_original += numeros[codigonumeros.index(c)]

print(frase_original)
        
