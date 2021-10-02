#Programa que converte um endereço IPv4 de decimal para Binário

endereco_atual = []
endereco_novo = []

for v in range(4):
    valor = int(input("Digite um número de até 3 dígitos e que seja menor ou igual a 255: "))
    while valor > 255 or valor < 0:
        valor = int(input("Valor inválido. Tente novamente: "))
    
    endereco_atual.append(str(valor))
    digitosBin = []
    
    #Convertendo para Binário em Ipv4 (8 bits)
    for binario in range(7, -1, -1):
        pos = 2 ** binario
        if valor >= pos:
            digitosBin.append("1")
            valor -= pos
        else:
            digitosBin.append("0")
        
    digitosBin = "".join(digitosBin)
    endereco_novo.append(digitosBin)

endereco_atual = ".".join(endereco_atual)
endereco_novo = ".".join(endereco_novo)

print(f"\nO endereco decimal {endereco_atual}"
    f"\ncorresponde a este endereco em binário: {endereco_novo}")
