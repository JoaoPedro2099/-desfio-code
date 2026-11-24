numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/": 
    if numero2 != 0:
        resultado = numero1 / numero2 
    else:
        resultado = "Erro: Divisão por zero"
else:
    resultado = "Operação inválida"

print(resultado)