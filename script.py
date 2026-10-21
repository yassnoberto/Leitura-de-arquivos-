# LEITURA DE ARQUIVO 
arquivo = open("arquivo.txt", "r") # r de read - ler 
conteudo = arquivo.read()
print(conteudo)
arquivo.close()