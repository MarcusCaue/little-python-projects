palavras = ["nome", "salario"]
tipos = ["String", "double"]

with open("methods.txt", "w") as arq:
    for i in palavras:
        arq.writelines(f"\npublic {tipos[palavras.index(i)]} get{i.capitalize()}() {'{'}\n    return this.{i};\n{'}'}\n")


        arq.writelines(f"\npublic void set{i.capitalize()}({tipos[palavras.index(i)]} new{i.capitalize()}) {'{'}\n    this.{i} = new{i.capitalize()};\n{'}'}\n")