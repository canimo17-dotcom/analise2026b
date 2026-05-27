# codigo que leia uma idade seguindo logica real, e imprima maior de ida de menor ou idoso
idade = int(input("Qual sua idade "))
if idade < 18:
     print("Menor de idade ")
elif idade >= 60:
    print("idoso ")  
else:
    print("Maior de idade ")      