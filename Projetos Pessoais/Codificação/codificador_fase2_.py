def fase2(entrada):
    # Produzido em grande parte por: Romero Galdino
    # Auxiliado e comentado: Marcus Cauê

    # Letras e símbolos que podem existir na frase
    # Chamarei essas strings de "CV"
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    minusculas = maiusculas.lower()
    numeros = "0123456789"

    # Letras e símbolos que estarão presentes na frase codificada
    # Chamarei essas strings de "CC"
    codigomaiusculas = "nijklmtuvwxyzabcdopqrsefgh*"
    codigominusculas = "ZAJKLMNOPQRSTUVWXYBCDEFGHI"
    codigonumeros = "5678920134"

    # Processamento
    novafrase = "" #Frase codificada no final
    for caracter in entrada:
        # Verifica se o "caracter" existe ou não em algumas das strings "CV"
        # Caso a condição seja verdadeira, a "novafrase" receberá o "caracter" sem ser codificado
        if ((caracter not in maiusculas) and (caracter not in minusculas) 
        and (caracter not in numeros)):
            novafrase += caracter
        else:
            """Caso o "caracter" exista em algumas das strings "CV", o mesmo será adicionado na "novafrase"
            na forma codificada"""
            if caracter in maiusculas: # Verifica se o "caracter" está na CV (maiusculas)
                novafrase += codigomaiusculas[maiusculas.index(caracter)]
            elif caracter in minusculas: # Verifica se o "caracter" está na CV (minusculas)
                novafrase += codigominusculas[minusculas.index(caracter)]
            elif caracter in numeros: # Verifica se o "caracter" está na CV (numeros)
                novafrase += codigonumeros[numeros.index(caracter)]
            
            # Caso alguma das condições forem verdadeiras, o "caracter" será codificado
            """Codificado: Troca o "caracter" que está em uma posição X em alguma das strings
            "CV" por um caracter que está na mesma posição X em alguma das strings "CC"."""
    
    return novafrase


print(fase2("Jonas de Samos"))
