# interface da calculadora
from calc2 import soma, sub, mult, div, porc

while True:
    # apresentação
    print('\n\t\t\t -- Calculadora 2 --\n')

    # Menu
    print('1. soma')
    print('2. subtração')
    print('3. multiplicação')
    print('4. divisão')
    print('5. porcentagem')
    print('6. Sair')

    # Ler a opção do usuário
    op = int(input('\nOpção: '))

    if op == 1 or op == 2 or op == 3 or op == 4 or op == 5:

        num1 = int(input('Informe o n1: '))
        num2 = int(input('Informe o n2: '))

        if op == 1:
            total = soma(num1, num2)
            print(f'{num1} + {num2} = {total}')

        elif op == 2:
            total = sub(num1, num2)
            print(f'{num1} - {num2} = {total}')

        elif op == 3:
            total = mult(num1, num2)
            print(f'{num1} * {num2} = {total}')

        elif op == 4:
          if num2 != 0:
            total = div(num1, num2)
            print(f'{num1} / {num2} = {total}')
          else:
             print('Erro: divisão por zero não permitida')
        elif op == 5:
            total = porc(num1, num2)
            print(f'{num1}/100 * {num2} = {total}')

    elif op == 6:
        print('Obrigado por me usar!')
        break

    else:
       print(f'Opção {op} Não existente!')
       break