numero_informado = int(input("Digite um número para checar se pertence à sequência de Fibonacci: "))
fibonacci = [0, 1]
numero_1 = 0
numero_2 = 1
proximo = 0

while fibonacci[-1] < numero_informado:
    proximo = numero_1 + numero_2
    numero_1 = numero_2
    numero_2 = proximo
    fibonacci.append(proximo)

if numero_informado in fibonacci:
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")

print(f"Sequência de Fibonacci gerada até o número {numero_informado}:")
print(fibonacci)

