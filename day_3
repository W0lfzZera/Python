#--------------------------------------------------------------#
# FOR:
"""

import time

for i in range(10):
    print(i + 1)

for i in range(50, 100 + 1, 2):     #INICIA O i COM 50 E VAI ATÉ 100 E CONTA DE 2 EM 2
    print(i)

for i in "Hector":
    print(i)

for second in range(10, 0, -1):
    print(second)
    time.sleep(1)                   #DELAY DE 1 SEGUNDO
print("Happy New Year!")

"""
#--------------------------------------------------------------#
# FOR ANINHADO:
"""

linha = int(input("Quantas linhas: "))
coluna = int(input("Quantas colunas: "))
simbolo = input("Digite o simbolo: ")

for i in range(linha):
    for j in range(coluna):
        print(simbolo, end = "")     #"end = "" " AO FINALIZAR UM CICLO NO LOOPING, CANCELA A QUEBRA DE LINHA
    print()                          #"print()" CRIA UMA QUEBRA DE LINHA

"""
#--------------------------------------------------------------#
# COMANDOS PARA CONTROLE DE LOOPING:

#"break" FINALIZA O LOOPING
#"continue" PULA UM CICLO DO LOOPING
#"pass" OCUPA UM ESPAÇO DO LOOPING
"""

while True:
    name = input("Digite seu nome: ")
    if name == "":
        print("Nome não recebido.")
    elif name != "":
        break

telefone = "123-456-7890"

for i in telefone:
    if i == "-":
        continue
    print(i, end = "")

for j in range(1, 21):
    if j == 13:
        pass
    else:
        print(j)

"""
#--------------------------------------------------------------#
# LISTAS:
"""

food = ["pizza", "hamburguer", "hotdog", "sushi"]

food[0] = "pudim"

#print(food[0])

food.append("sorvete")      #".append("string")" ADICIONA A STRING NO FINAL DA LISTA
food.remove("hotdog")       #".remove("string")" REMOVE A STRING DA LISTA
food.pop()                  #".pop()" REMOVE O ÚLTIMA STRING DA LISTA
food.insert(0,"bolo")       #".insert(n, "string")" ADICIONA A STRING NA POCIÇÃO n
food.sort()                 #".sort" ORGANIZA EM ORDEM ALFABÉTICA
food.clear()                #".clear()" REMOVE TODOS OS ELEMENTOS DA LISTA

for i in food:
    print(i)

"""
#--------------------------------------------------------------#
# LISTA 2D:
"""

bebidas = ["café", "chá", "energético"]
comida = ["pizza", "hamburguer", "hotdog"]
sobremesa = ["bolo", "sorvete"]

food = [bebidas, comida, sobremesa]

print(food[0][1])       # ACESSA A POSIÇÃO n DA VARIÁVEL E DENTRO DELA MOSTRA A STRING POSIÇÃO n

"""
#--------------------------------------------------------------#
# TUPLA:                            #SIMILAR A LISTA PORÉM É IMUDÁVEL
"""

estudante = ("Hector", 19, "homem")

print(estudante.count("Hector"))    #".count("string")" CONTA QUANTAS VEZES APARECE A STRING
print(estudante.index("homem"))     #".index("string")" CONTA QUE POSIÇÃO ESTÁ A STRING

for i in estudante:
    print(i)

if "Hector" in estudante:           #VERIFICA SE A STRING ESTÁ NA TUPLA
    print("Hector está aqui!!")

"""
#--------------------------------------------------------------#
