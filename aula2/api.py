# Criando uma API

import requests
import os

print('----------------- CONSULTA POKÉMON -----------------')
pokemon = input("Qual Pokémon deseja consultar? ").lower()

resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

dados = resposta.json()

os.system("cls")  # Limpa o terminal no Windows

print('----------------- DADOS POKÉMON -----------------')
print(f"NOME: {dados['name'].capitalize()}")
print(f"PESO: {dados['weight']}")
print(f"ALTURA: {dados['height']}")
print(f"TIPO: {dados['types'][0]['type']['name']}")
print('-------------------------------------------------')
