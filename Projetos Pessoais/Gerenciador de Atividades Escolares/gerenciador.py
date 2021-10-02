from datetime import datetime

diaAtual = datetime.today().day

with open("atividades.txt", "r") as arq:
    dados = arq.readlines()

    disciplinas = list()
    datas = list()
    for i in dados:
        materia_data = i.split(" -> ")
        disciplinas.append(materia_data[0])
        datas.append(materia_data[1])

print("=" * 50)
print("PRAZO DE ENTREGA DAS ATIVIDADES".center(50))
print("=" * 50)
print(f"{'DISCIPLINA':<20}    DATA DE ENTREGA\n")
for data in datas:
    diaDeEntrega = int(data[:2])

    if ((diaDeEntrega - diaAtual) <= 3):
        #ALTÍSSIMA
        prioridade = "\033[31mALTÍSSIMA\033[m"
    elif (((diaDeEntrega - diaAtual) <= 8)):
        #MEDIANA
        prioridade = "\033[33mMEDIANA\033[m"
    else:
        #TRANQUILO
        prioridade = "\033[32mTRANQUILO\033[m"

    print(f"-> {disciplinas[datas.index(data)]:<20} {data[:5]} -> {prioridade}")