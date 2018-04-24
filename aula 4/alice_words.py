# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Andre Moreno
# 1 semestre 2018

# Exercicio 20.8.3


import string

def cleanword(a):
    word = ""
    punctaction = "!\"#$%&'()*+,./:;<=>?@[\\]^_`{|}~"
    for letter in a:
        if letter == "-":
            word += " "
        elif letter not in punctaction:
            word += letter
    return word

def extract_words(w):
    w = cleanword(w)
    words = w.lower()
    return words.split()

#ler arquivo
arquivo = open('alice.txt', 'r')
texto = arquivo.read()

texto = extract_words(texto)

#ordenar lista
textosort = texto.sort()

#contar numero de palavras
dicionario = {}
for palavra in texto:
    if palavra[0] in string.ascii_letters:
        dicionario[palavra] = dicionario.get (palavra, 0) + 1

#abrir arquivo de saida
arquivo2 = open('alice_words.txt', 'w')

#impressao
tabulacao = "{0:<20} :  {1:<10}\n================================\n" .format("word", "count")
for x in dicionario:
    tabulacao = tabulacao +  "{0:<20} :  {1:<10}\n".format(x, dicionario[x])

arquivo2.write(tabulacao)
arquivo2.close()
arquivo.close()