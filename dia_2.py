#--------------------------------------------------------------#

# FUNÇÕES MATEMÁTICAS:
"""

import math            #IMPORTA A BIBLIOTECA MATH

pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))       #"ROUND(variável)" ARREDONDA O VALOR DA VARIÁVEL
print(math.ceil(pi))   #"MATH.CEIL(variável)" ARREDONDA O VALOR DA VARIÁVEL PARA CIMA
print(math.floor(pi))  #"MATH.FLOOR(vairável)" ARREDENDA O VALOR DA VARIÁVEL PARA BAIXO
print(abs(pi))         #"ABS(variável)" MOSTRA O VALOR ABSOLUTO DA VARIÁVEL
print(pow(pi, 2))      #"POW(variavel, n)" ELEVA O VALOR DA VARIÁVEL PELO NÚMERO DIGITADO
print(math.sqrt(pi))   #"MATH.SQRT(variável)" FAZ A RAIZ QUADRADA DO VALOR DA VARIÁVEL
print(max(x, y, z))    #"MAX(variáveis)" COMPARA QUAL A VARIÁVEL COM O MAIOR VALOR
print(min(x, y, z))    #"MIN(variáveis)" COMPARA QUAL A VARIÁVEL COM O MENOR VALOR

"""
#--------------------------------------------------------------#

# DIVIDINDO UMA STRING:

#SINTAXE: [START:STOP:STEP]
"""

name = "Hector Colchiesqui"
first_name = name[:6]        # [start:6]         #LÊ A STRING DO INÍCIO ATÉ A LETRA 6
last_name = name[7:]         # [7:end]           #LÊ A STRING DA LETRA 7 ATÉ O FINAL
funky_name = name[::2]       # [start:end:2]     #LÊ A STRING DO INÍCIO ATÉ O FINAL MAS PULANDO UMA LETRA
reversed_name = name[::-1]   # [start:end:-1]    #LÊ A STRING AO CONTRÁRIO

print(reversed_name)

website_1 = "http://google.com"
website_2 = "http://wikipedia.com"

slice = slice(7, -4)        #"SLICE(n, -n)" LÊ A STRING A PARTIR DA LETRA 7 E RETIRA 4 LETRAS DA DIREITA PRA ESQUEDA

print(website_1[slice])
print(website_2[slice])

"""
#--------------------------------------------------------------#

# IF:
"""

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are na adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")

"""
#--------------------------------------------------------------#

# OPERADORES LÓGICOS (AND, OR, NOT):
"""

temp = float(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):               #"NOT(termo da condição)" INVERTE O TRUE COM O FALSE E VISE-VERSA  
    print("The temperature is bad today!")
    print("Stay inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("Go outside")

"""
#--------------------------------------------------------------#

# WHILE:
"""

name = ""

while len(name) == 0:
    name = input("Enter your name: ")
print("Hello " + name)

"""
#--------------------------------------------------------------#
