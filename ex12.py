# codig que digte se for o nome senac, imprima 'seja bemvindo', senao "usuario nao identificado"
nome = input("Digite seu nome ").lower()
if nome == ("SENAC") :
    print("Seja Bem vindo Senac ")
else:
    print(f"Usuario {nome} não identificado")