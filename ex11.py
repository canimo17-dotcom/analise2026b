#leia o ano de nascimento eo atual, calcule a idade, >18 'maior de idade senao menor de idade
nasc= int(input( 'Digite seu ano de nascimento '))
ano = int(input("Digite o ano atual "))
data= ano - nasc
if data >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
