tabuada = int(input("Digite um número: "))
operador = input("Digite um operador: ")

for num in range(11):
    if operador == '*':
        print(f'{tabuada}{operador}{num} = ', tabuada*num)
    elif operador == '/':
        print(f'{tabuada}{operador}{num} = ', tabuada/num)
    elif operador == '-':
        print(f'{tabuada}{operador}{num} = ', tabuada-num)
    elif operador == '+':
        print(f'{tabuada}{operador}{num} = ', tabuada+num)
    elif operador == '**':
        print(f'{tabuada}{operador}{num} = ', tabuada**num)