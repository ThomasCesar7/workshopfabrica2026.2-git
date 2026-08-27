class Calculadora:
    def __init__(self):

        print('--------- Calculadora ---------')
        valor1 = float(input('Primeiro valor: '))
        valor2 = float(input('Segundo valor: '))
        print('Digite 1 para somar       (+)')
        print('Digite 2 para subtrair    (-)')
        print('Digite 3 para multiplicar (*)')
        print('Digite 4 para dividir     (/)')
        print('-------------------------------')

        while True:
            try:
                op = int(input('Informe a sua opção: '))

                if op == 1:
                    print(self.somar(valor1, valor2))

                elif op == 2:
                    print(self.subtrair(valor1, valor2))

                elif op == 3:
                    print(self.multiplicar(valor1, valor2))

                elif op == 4:
                    print(self.dividir(valor1, valor2))

                else:
                    print('OPÇÃO INVÁLIDA! ', end='')
                    continue
                break
            
            except ValueError:
                    print('OPÇÃO INVÁLIDA! ', end='')
                    continue


    # Métodos de cálculos
    def somar(self, valor1, valor2):
            return f'A soma: {valor1} + {valor2} = {valor1+valor2}'

    def subtrair(self, valor1, valor2):        
            return f'A subtração: {valor1} - {valor2} = {valor1-valor2}'
            
    def multiplicar(self, valor1, valor2):                
            return f'A multiplicação: {valor1} * {valor2} = {valor1*valor2}'

    def dividir(self, valor1, valor2):        
            return f'A Divisão: {valor1} / {valor2} = {valor1/valor2}'




c1 = Calculadora()