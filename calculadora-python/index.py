# Calculadora Simples

while True:
        
    print('\n\t\t\t -- Calculadora Simples --\n')
    
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Sair')

        
        # Entradas
        
    op = int(input('\n\t Opção: '))   
         
        # Processamento 
        
    if op == 1:
            print('\n\t\t\t -- Soma -- \n')
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            resultado = num1 + num2
            print('Resultado: ', resultado)
            
    elif op == 2:
            print('\n\t\t\t -- Subtração -- \n')
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo númeoro: '))
            resultado = num1 - num2 
            print('Resultado:  ', resultado)

    elif op == 3:
            print('\n\t\t\t -- Multiplicação -- \n')
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            resultado = num1 * num2
            print('Resultado: ', resultado)

    elif op == 4:
            print('\n\t\t\t -- Divisão -- \n')
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            resultado = num1 / num2
            print('Resultado: ', resultado)
            
               
        # Saída
        
    elif op == 5:
        print('\n Forte abraço! \n')
        break
    else:
        print('Opção {} incorreta'.format(op))