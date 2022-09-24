atributos = ["titulo", "autor", "totPaginas", "pagAtual", "aberto", "leitor"]
tipos = ["String", "String", "short", "short", "boolean", "Pessoa"]

with open("methods.txt", "w") as arq:
    for atrbt in atributos:
        arq.writelines(f"\npublic {tipos[atributos.index(atrbt)]} get{atrbt.capitalize()}() {'{'}\n    return this.{atrbt};\n{'}'}\n")


        arq.writelines(f"\npublic void set{atrbt.capitalize()}({tipos[atributos.index(atrbt)]} new{atrbt.capitalize()}) {'{'}\n    this.{atrbt} = new{atrbt.capitalize()};\n{'}'}\n")