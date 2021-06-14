# -*- coding: utf-8 -*-
"""PrimeirosPassos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_pmhejQ9HCVeNcouF3kEip2zzeyNHuAn

# Primeira Função
"""

def saudacao():
  nome = input('Qual o seu nome? ')
  print(f'Seja bem-vindo, {nome}')

saudacao()

"""# Função com parâmetros"""

def saudacao_com_parametros(nome_da_pessoa) :
  print(f'Olá {nome_da_pessoa}')

nome = 'Iuri'

saudacao_com_parametros(nome)



"""# Condicional"""

def verifica_se_pode_dirigir():
  idade = input('Qual a sua idade? ')
  idade = int(idade)
  if (idade >= 18):
    print('Pode dirigir.')
  else:
    print('Não pode dirigir.')

verifica_se_pode_dirigir()

"""# Lista"""

idades = [18,16,22,15]

def verifica_se_pode_dirigir(idade):
  if (idade >= 18):
    print(f'{idade} anos. Pode dirigir.')
  else:
    print(f'{idade} anos. Não pode dirigir.')

for idade in idades:
  verifica_se_pode_dirigir(idade)



"""# Notas aleatorias"""

from random import randrange, seed

seed(11)

randrange(0,11)

notas_matematica = []

for nota in range(8):
  notas_matematica.append(randrange(0,11))

print(notas_matematica)

"""# Matplotlib"""

from matplotlib import pyplot as plt


x = list(range(1, 9))
y = notas_matematica

plt.plot(x, y)
plt.title("Notas de matemática")
plt.xlabel("Provas")
plt.ylabel("Notas")
plt.show()

