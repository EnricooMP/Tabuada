valor = int(input("Escolha um valor de (1-10): "))
print(f'\nTabuada do {valor}')

for multiplicador in range (1, 11):
    resultado = valor * multiplicador
    print(f"\n{valor} x {multiplicador} = {resultado}")
