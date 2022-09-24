def criaCodigoBaseEmJava(nomeArquivo, nomeClasse, nomeMetodo="main"):
    arq = open(nomeArquivo, "w")

    codigoBaseJava = ["public class %s {\n" %nomeClasse, "  public static void %s(String[] args) {\n" %nomeMetodo, "        \n", "    }\n", "}\n"]

    arq.writelines(codigoBaseJava)
    arq.close()

arquivos = ["NumPrimo", "Main", "NumInteiro", "ManipulacaoString"]
for arquivo in arquivos:
    criaCodigoBaseEmJava(f"{arquivo}.java", f"{arquivo}")