from random import randint


usuarios = [
    {'nome': 'Thomás'},     #[0]
    {'nome': 'Rafael'},     #[1]
    {'nome': 'Pedro'},      #[2]
    {'nome': 'Ricardo'},    #[3]
    {'nome': 'Gabriel'},    #[4]
]

def soma(a, b):
    total = a + b
    return f'Somou {a} + {b} e deu {total:^5}'

i = 0
print(f'{"NOME":<10}{"RESULTADO":^25}')
for usuario in usuarios:
    valor1 = randint(0, 10)
    valor2 = randint(0, 10)

    print(f'{usuario['nome']:<10} {soma(valor1, valor2):<30}')
    i+=1
