string_padrao = "nenhuma string foi fornecida pelo usuário"

print("Digite 1 caso deseje fornecer uma string; ou 2 caso deseje utilizar a padrão")
opcao = int(input("Qual é a sua opção: "))

while opcao != 1 and opcao != 2:
    print("Opção inválida. Digite novamente.")
    opcao = int(input("Qual é a sua opção: "))

if opcao == 1:
    string_fornecida = input("Digite a string que deseja inverter: ")
    string_a_inverter = string_fornecida

if opcao == 2:
    string_a_inverter = string_padrao

string_invertida = ""
for cont in range(len(string_a_inverter) - 1, -1, -1):
    string_invertida += string_a_inverter[cont]

print("String original:", string_a_inverter)
print("String invertida:", string_invertida)
