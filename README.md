# 🔐 Gerador de Senhas Aleatórias em Python

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

## 📚 Sobre o Projeto

O **Gerador de Senhas Aleatórias** é um projeto simples em Python que permite criar senhas seguras e personalizadas diretamente pelo terminal. Você pode definir o tamanho da senha e escolher se deseja incluir letras maiúsculas, minúsculas, números e símbolos.

Ótimo para quem quer praticar manipulação de strings, listas e funções em Python!

---

## 🛠️ Como Usar

1. **Clone o repositório:**
git clone https://github.com/seuusuario/gerador-senhas.git
cd gerador-senhas

text

2. **Execute o script:**
python gerador_senhas.py

text

3. **Siga as instruções no terminal para personalizar e gerar sua senha.**

---

## 💻 Exemplo de Uso

Bem-vindo ao Gerador de Senhas!
Quantos caracteres você deseja? 12
Incluir letras maiúsculas? (s/n): s
Incluir letras minúsculas? (s/n): s
Incluir números? (s/n): s
Incluir símbolos? (s/n): n
Sua senha gerada: 3kQb7FvR2wLp

text

---

## 🧩 Código Fonte

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

text

---

## 📦 Requisitos

- Python 3.8 ou superior

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## 📝 Licença

Este projeto está sob a licença MIT.

---

## 📫 Contato

Dúvidas ou sugestões? Abra uma issue ou envie um e-mail para seuemail@exemplo.com

---
