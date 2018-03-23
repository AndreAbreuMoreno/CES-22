readfile = open("entradaCap13.1", "r")
file = readfile.readlines()
readfile.close()

#verificar quantas linhas há no arquivo
print("{}".format(file))
sz = len(file)
sz -= 1


writefile = open("saida.txt", "w")
while sz >= 0:
    writefile.write(file[sz])
    sz -= 1

writefile.close