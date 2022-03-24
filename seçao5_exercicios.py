import math
"""
# 1:
num1 = int(input("Escreva um número: "))
num2 = int(input("Escreva outro número: "))
if num1 < num2:
    print("O segundo número é o maior.")
else:
    print("O primeiro numéro é o maior.")

# 2:
numero = int(input("Escreva um número: "))
if numero > 0:
    print(math.sqrt(numero))
else:
    print("Número inválido.")

# 3:
numero = float(input("Escreva um número: "))
if numero > 0:
    print(math.sqrt(numero))
else:
    print(numero ** 2)

# 4:
numero = int(input("Escreva um número: "))
if numero > 0:
    print(f"Quadrado do número: {numero ** 2};")
    print(f"Raiz quadrada: {math.sqrt(numero)}.")
else:
    print("Número inválido.")

# 5:
numero = int(input("Escreva um número: "))
if (numero % 2) == 0:
    print("Par.")
else:
    print("Ímpar.")

# 6:
num1 = int(input("Escreva um número: "))
num2 = int(input("Escreva outro número: "))
if num1 > num2:
    print("Primeiro número é maior")
    print(f"E a diferença entre eles é: {num1 - num2}")
else:
    print("O segundo número é maior;")
    print(f"E a diferença entre eles é: {num2 - num1}")

# 7:
num1 = int(input("Escreva um número: "))
num2 = int(input("Escreva outro número: "))
if num1 > num2:
    print("O primeiro número é maior;")
elif num1 == num2:
    print("Números iguais.")
else:
    print("O segundo número é maior.")

# 8:
nota1 = float(input("Escreva a primeira nota: "))
nota2 = float(input("Escreva a segunda nota: "))
if nota1 and nota2 <= 10:
    print(f"A média dessas notas é: {round((nota1 + nota2) / 2, 2)}.")
else:
    print("Esse número não é uma nota válida, favor, utilizar valores entre 0 e 10.")

# 9:
salario = float(input("Escreva seu salário: "))
emprestimo = float(input("Escreva o valor da prestação do empréstimo: "))
porcentagem = salario * 20 / 100
if emprestimo > porcentagem:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")

# 10:
altura = float(input("Escreva a sua altura: "))
sexo = input("Escreva seu sexo(Masculino ou feminino): ")
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7
if sexo == "masculino" or "Masculino" or "Homem" or "homem":
    print(f"Peso ideal: {peso_ideal_homem}.")
else:
    print(f"Peso ideal: {peso_ideal_mulher}.")

# 11:
num = int(input("Escreva um número: "))
digito = num // 100
digito2 = num % 100 // 10
digito3 = num % 10
if num <= 999:
    print(f"A soma dos dígitos do número é: {digito + digito2 +digito3}")
else:
    print("Número inválido.")

# 12:
num = int(input("Escreva um número: "))
if num < 0:
    print("Número inválido.")
else:
    print(f"O logaritmo do número escrito é: {math.log(num)}")

# 13:
nota1 = float(input("Escreva a primeira nota: "))
nota2 = float(input("Escreva a segunda nota: "))
nota3 = float(input("Escreva a terceira nota: "))
media_ponderada = (nota1 + nota2 + (nota3 * 2)) / 3
print()
print(f"A média do aluno ficou: {media_ponderada}")
print()
if media_ponderada < 6.0:
    print(f"Reprovado.")
else:
    print(f"Aprovado.")

# 14:
trabalho_lab = float(input("Escreva sua nota do trabalho de laboratório: "))
avaliacao_sem = float(input("Escreva sua nota da avaliação semestral: "))
exame_final = float(input("Escreva sua nota do exame final: "))
media_final = ((trabalho_lab * 2) + (avaliacao_sem * 3) + (exame_final * 5)) / 3
print()
print(media_final)
print()
if media_final <= 2.9:
    print("Reprovado.")
elif media_final <= 4.9:
    print("Recuperação.")
else:
    print("Aprovado.")

# 15:
a = "segunda-feira"
b = "terça-feira"
c = "quarta-feira"
d = "quinta-feira"
e = "sexta-feira"
f = "sábado"
num = int(input("Escreva um número: "))
if num == 1:
    print(f"Hoje é {a}.")
elif num == 2:
    print(f"Hoje é {b}.")
elif num == 3:
    print(f"Hoje é {c}.")
elif num == 4:
    print(f"Hoje é {d}.")
elif num == 5:
    print(f"Hoje é {e}.")
elif num == 6:
    print(f"Hoje é {f}.")
else:
    print("Número inválido.")

# 16:
a = "janeiro"
b = "fevereiro"
c = "março"
d = "abril"
e = "maio"
f = "junho"
g = "julho"
h = "agosto"
i = "setembro"
j = "outubro"
k = "novembro"
l = "dezembro"
num = int(input("Escreva um número: "))
if num == 1:
    print(f"Estamos em {a}.")
elif num == 2:
    print(f"Estamos em {b}.")
elif num == 3:
    print(f"Estamos em {c}.")
elif num == 4:
    print(f"Estamos em {d}.")
elif num == 5:
    print(f"Estamos em {e}.")
elif num == 6:
    print(f"Estamos em {f}.")
elif num == 7:
    print(f"Estamos em {g}.")
elif num == 8:
    print(f"Estamos em {h}.")
elif num == 9:
    print(f"Estamos em {i}.")
elif num == 10:
    print(f"Estamos em {j}.")
elif num == 11:
    print(f"Estamos em {k}.")
elif num == 12:
    print(f"Estamos em {l}.")
else:
    print("Número inválido.")

# 17:
B = int(input("Base maior: "))
b = int(input("Base menor: "))
h = int(input("Altura: "))
area = (B + b) * h / 2
if B and b < 0:
    print("Bases inválidas.")
else:
    print(f"A área do trapézio é {area}")

# 18:
print("a) Adição")
print("b) Subtração")
print("c) Multiplicação")
print("d) Divisão")
opcao = input("Escreva sua opção: ")
num1 = int(input("Esceva o primeiro número: "))
num2 = int(input("Escreva o segundo número: "))
if opcao == "a":
    print(f"A soma é {num1 + num2}.")
elif opcao == "b":
    print(f"A subtração é {num1 - num2}.")
elif opcao == "c":
    print(f"A multiplicação é {num1 * num2}.")
elif opcao == "d":
    print(f"A divisão é {num1 / num2}.")
else:
    print("Opção inválida.")

# 19:
num = int(input("Escreva um número: "))
if num % 3 == 0 and num % 5 == 0:
    print("Número divisível pelas duas opções.")
elif num % 3 == 0:
    print("Número divisível por 3.")
elif num % 5 == 0:
    print("Número divisível por 5.")
else:
    print("Número indivisível por 3 ou 5.")

# 20:
A = int(input("Escreva o valor do lado A: "))
B = int(input("Escreva o valor do lado B: "))
C = int(input("Escreva o valor do lado C: "))
if A < B + C and B < A + C and C < A + B:
    if A == B and A == C:
        print("Triângulo Equilátero.")
    elif A == B and A != C:
        print("Triângulo Isósceles.")
    elif A != B and A != C:
        print("Triângulo Escaleno.")
    else:
        pass
else:
    print("Lados inválidos.")

# 21:
print("1- Adição")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")
opcao = str(input("Escreva sua opção: "))
num1 = int(input("Esceva o primeiro número: "))
num2 = int(input("Escreva o segundo número: "))
if opcao == "1":
    print(f"A soma é {num1 + num2}.")
elif opcao == "2":
    print(f"A subtração é {num1 - num2}.")
elif opcao == "3":
    print(f"A multiplicação é {num1 * num2}.")
elif opcao == "4":
    print(f"A divisão é {num1 / num2}.")
elif opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
    print("ERRO 404: Opção inválida.")
else:
    print()

# 22:
idade = int(input("Escreva sua idade: "))
tempo_servico = int(input("Escreva seu tempo de serviço: "))
if idade >= 65:
    print("Você pode aposentar por idade.")
elif tempo_servico >= 30:
    print("Você pode aposentar por tempo trabalhado.")
elif idade >= 60 and tempo_servico >= 25:
    print("Você pode aposentar por idade e tempo trabalhado.")
else:
    print("Você não pode aposentar.")

# 23:
ano = int(input("Escreva o ano: "))
if ano % 400 == 0 or ano % 4 == 0 or ano % 100 == 1:
    print("Esse ano é bissexto.")
else:
    print("Esse ano não é bissexto.")

# 24:
MG = 107 / 100
SP = 112 / 100
RJ = 115 / 100
MS = 108 / 100
valor = int(input("Escreva o valor do produto: "))
estado_destino = input("Escreva o estado de destino(favor usar a sigla e em maiúsculo, exemplo: RJ): ")
if estado_destino == "MG":
    print(f"O valor final é {valor * MG} reais.")
elif estado_destino == "SP":
    print(f"O valor final é {valor * SP} reais.")
elif estado_destino == "RJ":
    print(f"O valor final é {valor * RJ} reais.")
elif estado_destino == "MS":
    print(f"O valor final é {valor * MS} reais.")
else:
    print("Esse estado não existe na lista.")

# 25:
a = float(input("Escreva o valor de a: "))
b = float(input("Escreva o valor de b: "))
c = float(input("Escreva o valor de c: "))
delta = (b ** 2) - 4 * a * c
if delta < 0:
    print("Não existe raiz.")
elif delta > 0:
    x = -b + math.sqrt(delta) / 2 * a
    x1 = -b - math.sqrt(delta) / 2 * a
    print(f"As raízes são {round(x, 2)} e {round(x1, 2)}, respectivamente.")
elif delta == 0:
    x = -b + math.sqrt(delta) / 2 * a
    print(f"A raiz é {round(x, 2)}.")
else:
    print("Isso não é uma equação do segundo grau.")

# 26:
km = int(input("Escreva os km percorridos: "))
l = int(input("Escreva quantos litros foram gastos: "))
total = km / l
if total <= 8:
    print("Venda o carro.")
elif total <= 14:
    print("Econômico.")
elif total > 12:
    print("Super econômico.")
else:
    print()

# 27:
idade = int(input("Escreva a sua idade: "))
if idade == 5 or idade == 6 or idade == 7:
    print("Infantil A.")
elif idade == 8 or idade == 9 or idade == 10:
    print("Infantil B.")
elif idade == 11 or idade == 12 or idade == 13:
    print("Juvenil A.")
elif idade == 14 or idade == 15 or idade == 16 or idade == 17:
    print("Juvenil B.")
elif idade >= 18:
    print("Sênior.")
else:
    print("Não possui idade adequada.")

# 28:
print("1 - Geométrica")
print("2 - Ponderada")
print("3 - Harmônica")
print("4 - Aritmética")
opcao = str(input("Escreva a opção desejada: "))
x = int(input("Escreva o valor de x: "))
y = int(input("Escreva o valor de y: "))
z = int(input("Escreva o valor de z: "))
if opcao == "1":
    geometrica = (x ** 1/3) * (y ** 1/3) * (z ** 1/3)
    print(f"A raiz geométrica é {geometrica}.")
elif opcao == "2":
    peso1 = int(input("Escreva o peso do primeiro número: "))
    peso2 = int(input("Escreva o peso do segundo número: "))
    peso3 = int(input("Escreva o peso do terceiro número: "))
    ponderada = (x * peso1) + (y * peso2) + (z * peso3) / 6
    print(f"A média ponderada é {ponderada}.")
elif opcao == "3":
    harmonica = 1 / (1 / x) + (1 / y) + (1 / z)
    print(f"A média harmônica é {harmonica}.")
elif opcao == "4":
    aritmetica = (x + y + z) / 3
    print(f"A média aritmética é {aritmetica}.")
else:
    print("Não foi possível calcular a média, pois a opção não é valida.")

# 29:
print("1 - Qual é a soma de 5 + 20?")
resposta1 = int(input("Escreva a resposta: "))
if resposta1 == 25:
    print("Você acertou a pergunta número 1.")
    resposta1 = 1
else:
    print("Você errou essa pergunta. A resposta correta é 25.")
    resposta1 = 0

print("2 - Qual é a soma de 10 + 32? ")
resposta2 = int(input("Escreva a resposta: "))
if resposta2 == 42:
    print("Você acertou a pergunta número 2.")
    resposta2 = 1
else:
    print("Você errou essa pergunta. A resposta correta é 42.")
    resposta2 = 0

print("3 - Qual é a soma de 7 + 33? ")
resposta3 = int(input("Escreva a resposta: "))
if resposta3 == 40:
    print("Você acertou a pergunta número 3.")
    resposta3 = 1
else:
    print("Você errou essa pergunta. A resposta correta é 40.")
    resposta3 = 0

print("4 - Qual é a soma de 21 + 62? ")
resposta4 = int(input("Escreva a resposta: "))
if resposta4 == 83:
    print("Você acertou a pergunta número 4.")
    resposta4 = 1
else:
    print("Você errou essa pergunta. A resposta correta é 83.")
    resposta4 = 0

print("5 - Qual é a soma de 20 + 52? ")
resposta5 = int(input("Escreva a resposta: "))
if resposta5 == 72:
    print("Você acertou a pergunta número 5!")
    resposta5 = 1
else:
    print("Você errou essa pergunta. A resposta correta é 72.")
    resposta5 = 0

soma_respostas = resposta1 + resposta2 + resposta3 + resposta4 + resposta5

if soma_respostas == 5:
    print("Você acertou todas as respostas.")
elif soma_respostas == 4:
    print("Você acertou 4/5 respostas.")
elif soma_respostas == 3:
    print("Você acertou 3/5 respostas.")
elif soma_respostas == 2:
    print("Você acertou 2/5 respostas.")
elif soma_respostas == 1:
    print("Você acertou 1/5 respostas.")
else:
    print("Você não acertou nenhuma das respostas.")

# 30:
a = int(input("Escreva o primeiro número: "))
b = int(input("Escreva o segundo número: "))
c = int(input("Escreva o terceiro número: "))

if a < b < c:
    print(f"{a}, {b}, {c}.")
elif a < c < b:
    print(f"{a}, {c}, {b}.")
elif b < a < c:
    print(f"{b}, {a}, {c}.")
elif b < c < a:
    print(f"{b}, {c}, {a}.")
elif c < a < b:
    print(f"{c}, {a}, {b}.")
elif c < b < a:
    print(f"{c}, {b}, {a}.")
else:
    print()

# 31:
altura = float(input("Escreva sua altura(exemplo: 1.10): "))
peso = float(input("Escreva seu peso: "))
if altura < 1.20 and peso <= 60:
    print("Essa pessoa pertence à classe: A")
elif altura >= 1.20 and altura <= 1.70 and peso <= 60:
    print("Essa pessoa pertence à classe: B")
elif altura > 1.70 and peso <= 60:
    print("Essa pessoa pertence à classe: C")
elif altura < 1.20 and peso >= 60 and peso <= 90:
    print("Essa pessoa pertence à classe: D")
elif altura >= 1.20 and altura <= 1.70 and peso >= 60 and peso <= 90:
    print("Essa pessoa pertence à classe: E")
elif altura > 1.70 and peso >= 60 and peso <= 90:
    print("Essa pessoa pertence à classe: F")
elif altura < 1.20 and peso >= 60 and peso > 90:
    print("Essa pessoa pertence à classe: G")
elif altura >= 1.20 and altura <= 1.70 and peso > 90:
    print("Essa pessoa pertence à classe: H")
elif altura > 1.70 and peso > 90:
    print("Essa pessoa pertence à classe: I")
else:
    print("Essas informações são inválidas ou não estão contidas na tabela de referência.")

# 32:
print(f"Cachorro Quente - 100\n"
      "Bauru Simples - 101\n"
      "Bauru com ovo - 102\n"
      "Hamburguer - 103\n"
      "Cheeseburguer - 104\n"
      "Suco - 105\n"
      "Refrigerante - 106")

pedido = str(input("Escreva o código do produto que deseja: "))

if pedido == "100":
    print(f"O seu pedido foi um cachorro quente de 1.20 reais. ")
elif pedido == "101":
    print("O seu pedido foi um bauru simples de 1.30 reais.")
elif pedido == "102":
    print("O seu pedido foi um bauru com ovo de 1.50 reais.")
elif pedido == "103":
    print("O seu pedido foi um hamburger de 1.20 reais.")
elif pedido == "104":
    print("O seu pedido foi um cheeseburguer de 1.70 reais.")
elif pedido == "105":
    print("O seu pedido foi um suco de 2.20 reais.")
elif pedido == "106":
    print("O seu pedido foi um refrigerante de 1.00 reais.")

# 33:

preco = int(input("Escreva o preço: "))
if preco <= 50:
    preco_novo = preco * (5 / 100) + preco
    print(preco_novo)
elif preco > 50 and preco <= 100:
    preco_novo = preco * (10 / 100) + preco
    print(preco_novo)
elif preco > 100:
    preco_novo = preco * (15 / 100) + preco
    print(preco_novo)
else:
    print()

if preco_novo <= 80:
    print("Barato.")
elif preco_novo > 80 and preco_novo <= 120:
    print("Normal.")
elif preco_novo > 120 and preco_novo <= 200:
    print("Caro.")
elif preco_novo > 200:
    print("Muito caro.")
else:
    print()

# 34:
nota = float(input("Escreva sua nota: "))
faltas = int(input("Escreva quantas faltas você obteve: "))
if nota <= 10.0 and nota >= 9.0:
    if faltas <= 20:
        print("Você obeteve conceito A.")
    else:
        print("Você obeteve conceito B.")
elif nota <= 8.9 and nota >= 7.5:
    if faltas <= 20:
        print("Você obeteve conceito B.")
    else:
        print("Você obeteve conceito C.")
elif nota <= 7.4 and nota >= 5.0:
    if faltas <= 20:
        print("Você obeteve conceito C.")
    else:
        print("Você obeteve conceito D.")
elif nota <= 4.9 and nota >= 4.0:
    if faltas <= 20:
        print("Você obeteve conceito D.")
    else:
        print("Você obeteve conceito E.")
elif nota <= 3.9 and nota >= 0.0:
    if faltas <= 20:
        print("Você obteve conceito E.")
    else:
        print("Você obteve conceito E.")
else:
    print()

# 35:
dia = int(input("Escreva o dia (1): "))
mes = int(input("Escreva o mês (4): "))
ano = int(input("Escreva o ano (2000): "))

valida = False

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    if dia <= 31:
        valida = True
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        valida = True
elif mes == 2:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        if dia <= 29:
            valida = True
    elif dia <= 28:
        valida = True

if valida:
    print("Valida.")
else:
    print("Inválida.")
# 36
venda_mensal = int(input("Escreva a quantia de venda mensal: "))

if venda_mensal >= 100000:
    comissao = 700 + (16 / 100 * venda_mensal)
    print(f"A comissão foi de {comissao}; Tudo ficou em: {venda_mensal+comissao}")
elif venda_mensal < 100000 and venda_mensal >= 80000:
    comissao = 650 + (14 / 100 * venda_mensal)
    print(f"A comissão foi de {comissao}; Tudo ficou em: {venda_mensal+comissao}")
elif venda_mensal < 80000 and venda_mensal >= 60000:
    comissao = 600 + (14 / 100 * venda_mensal)
    print(f"A comissão foi de {comissao}; Tudo ficou em: {venda_mensal+comissao}")
elif venda_mensal < 60000 and venda_mensal >= 40000:
    comissao = 550 + (14 / 100 * venda_mensal)
    print(f"A comissão foi de {comissao}; Tudo ficou em: {venda_mensal+comissao}")
elif venda_mensal < 40000 and venda_mensal >= 20000:
    comissao = 500 + (14 / 100 * venda_mensal)
    print(f"A comissão foi de {comissao}; Tudo ficou em: {venda_mensal+comissao}")
elif venda_mensal < 20000:
    comissao = 400 + (14 / 100 * venda_mensal)
    print(f"A comissão foi de {comissao}; Tudo ficou em: {venda_mensal+comissao}")
"""
# 37:

