# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)

idade = int(input("digite a idade"))

if idade <=0 : print("você é uma criança!")
elif idade <=17 : print("você é um adolescente!")
elif idade >=18 : print ("você é um adulto!")
if idade >=60 : print("você é idoso!")