# importa as bibliotecas
import os
import time

# usuário informa um número
contador = int(input('Informe um número inteiro: '))
os.system('cls')

# conta a parir do número informado até o 0
while contador >= 0:
    print(f'Contagem regressiva: {contador}...')
    time.sleep(1)
    os.system('cls')
    contador -= 1

print('BOOM!!!!')
    