
#ler todas as linhas do aquivo e armazenar as linhas
#em uma lista
ent = open("entradaCap13.1.txt", "r")
arquivo = ent.readlines()
ent.close()

#Olhar o tamanho do arquivo
sz = len(arquivo)
sz -= 1

#ler toda a lista e armazenar em um arquivo saida na
#ordem inversa
saida = open("saidaCap13.1.txt", "w")
while sz >= 0:
    saida.write(arquivo[sz])
    sz -= 1

saida.close

