import random
import string

print("Bem-vindo ao Gerador de Senhas!")

tamanho = int(input("Quantos caracteres você deseja? "))
maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
numeros = input("Incluir números? (s/n): ").lower() == 's'
simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

caracteres = ''
if maiusculas:
  caracteres += string.ascii_uppercase
if minusculas:
  caracteres += string.ascii_lowercase
if numeros:
  caracteres += string.digits
if simbolos:
  caracteres += string.punctuation

if not caracteres:
  print("Você deve selecionar pelo menos um tipo de caractere!")
else:
  senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
  print("Sua senha gerada:", senha)
