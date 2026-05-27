#leia um valor e imprima se o valor esta dentro de 0e10 11e20 21e30 ou maior que 30
valor = int(input("Digite um valor "))
if valor >= 0 and valor <= 10:
    print(f"O valor {valor}, esta na faixa entre 0 e 10")
elif valor > 10 and valor <= 20:
    print(f" O valor {valor}, esta na faixa entre 11 e 20")    
elif valor > 20 and valor <= 30:
    print(f"O valor {valor}, esta na faixa entre 21 e 30")
else:
    print(f"O valor esta na faixa maior que 30")   
    print("teste")



   

   