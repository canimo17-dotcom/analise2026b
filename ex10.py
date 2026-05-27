# if: Codigo que leia dois valores, calcule a media. se a media for maior que 5 imprima aprovado, senao imprima recuperacao
nota1 = float(input("digite sua primeira nota "))
nota2 = float(input("digite sua segunda nota "))
resultado = (nota1 + nota2) /2
if resultado > 5:
    print(f"Aluno provado com nota {resultado} ")
else:
    print(f"Aluno em recuperação com nota {resultado}")


