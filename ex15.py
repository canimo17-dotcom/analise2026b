#alistamento militar acima de 18 anos
genero = input("Digite M- Masculino e F- Feminino ").upper()
idade = int(input("digite sua idade "))
if idade >= 18 and genero == "m":
    print("Voce está apto para ingressar ")

else:
    print("Voce não está apto")   
  

