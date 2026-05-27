# codigo que leia dois valores e diga qual o maior entre eles
valor1 = float(input("Digite um numero "))
valor2 = float(input("Digite outro numero "))
if valor1 > valor2:
    print(f"O valor maior é {valor1}")
elif valor2 > valor1:
    print(f"O valor maior é {valor2}")  
else:
    print(f"Os valores são iguais")      
