# TIPOS DE VARIÁVEIS:

#--------------------------------------------------------------#

# STRING:

#name = "Hector"
#print(name)
#print(type(name))   #"TYPE(variavel)" MOSTRA O TIPO DA VARIÁVEL

#first_name = "Hector"
#last_name = "Colchiesqui"
#full_name = first_name + " " + last_name
#print(full_name)

#--------------------------------------------------------------#

# INT:

#age = 19
#age = age + 1
#age += 1
#print("Your age is: " + str(age))   #"STR(variavel)" CONVERTE UM INT OU UM FLOAT PARA UMA STRING

#--------------------------------------------------------------#

# FLOAT:

#height = 1.72
#print("Your height is: " + str(height) + "m")
#print(type(height))

#--------------------------------------------------------------#

# BOOL:

#human = True
#print("Are you a human: " + str(human))
#print(type(human))

#--------------------------------------------------------------#

# MULTIPLOS TIPOS DE VARIÁVEIS:

#name, age, attractive = "Hector", 19, True
#print(name)
#print(age)
#print(attractive)

#Bob_Esponja = Patrick = Sandy = Lula_Molusco = 30
#print(Bob_Esponja)
#print(Patrick)
#print(Sandy)
#print(Lula_Molusco)

#--------------------------------------------------------------#

# METÓDOS DE STRING:

#name = "Hector"

#print(len(name))                  #"LEN(variavel)" CONTA QUANTOS ESPAÇOS FORAM USADOS NA STRING
#print(name.find("t"))             #".FIND("letra")" MOSTRA EM QUE POSIÇÃO ESTÁ A LETRA SELECIONADA
#print(name.capitalize())          #".CAPITALIZE()" INICIA A STRING COM A PRIMEIRA LETRA MAIÚSCULA
#print(name.upper())               #".UPPER()" FAZ COM QUE A STRING FIQUE EM MAIÚSCULA
#print(name.lower())               #".LOWER()" FAZ COM QUE A STRING FIQUE EM MINÚSCULA
#print(name.isdigit())             #".ISDIGIT()" VERIFICA SE A STRING É UMA COMBINAÇÃO DE NÚMEROS
#print(name.isalpha())             #".ISALPHA()" VERIFICA SE A STRING É UMA COMBINAÇÃO DE LETRAS
#print(name.count("o"))            #".COUNT("letra")" CONTA QUANTAS DA LETRA ESCOLHIDA TEM NA STRING
#print(name.replace("o", "e"))     #".REPLACE("letra1", "letra2")" MUDA A LETRA SELECIONADA DA STRING POR OUTRA DIGITADA
#print(name*3)                     #"*n" REPETE A STRING O NÚMERO DE VEZES DIGITADA

#--------------------------------------------------------------#

# CONVERTENDO TIPOS DE VARIÁVEIS:

#x = 1
#y = 2.0
#z = "3"

#x = float(x)    #"FLOAT(variavel)" CONVERTE O TIPO DA VARIÁVEL PARA FLOAT
#y = str(y)      #"STR(variavel)" CONVERTE O TIPO DA VARIÁVEL PARA STRING
#z = int(z)      #"INT(variavel)" CONVERTE O TIPO DA VARIÁVEL PARA INT

#print(x)
#print(y)
#print(z * 3)

#--------------------------------------------------------------#

# USANDO O INPUT:

#name = input("What is your name?: ")            #"INPUT("")" RECEBE A STRING QUE O USUÁRIO DIGITAR, FUNCIONA COMO UM PRINTF E UM SCANF JUNTOS
#age = int(input("How old are you?: "))
#height = float(input("How tall are you?: "))

#age = age + 1

#print("Hello " + name)
#print("So you are " + str(age) + " years old")
#print("So you are " + str(height) + "m tall")

#--------------------------------------------------------------#