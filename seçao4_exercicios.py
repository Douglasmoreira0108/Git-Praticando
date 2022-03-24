"""
# 1:
numero_int = int(input("Escreva um número: "))
print(numero_int)

# 2:
numero_real = float(input("Escreva um número: "))
print(numero_real)

# 3:
numero1 = int(input("Escreva o primeiro número: "))
numero2 = int(input("Escreva o segundo número: "))
numero3 = int(input("Escreva o terceiro número: "))
soma = numero1 + numero2 + numero3
print(soma)

# 4:
numero_real = float(input("Escreva um número: "))
quadrado = int(numero_real * numero_real)
print(quadrado)

# 5:
numero_real = float(input("Escreva um número: "))
divisao = int(numero_real/5)
print(divisao)

# 6:
temp_celsius = int(input("Escreva a temperatura em Celsius: "))
temp_fahrenheit = int(temp_celsius * (9.0/5.0) + 32.0)
print(f'{temp_fahrenheit}° Fahrenheit.')

# 7:
temp_fahrenheit = int(input("Escreva a temperatura em Fahrenheit: "))
temp_celsius = int(5.0 * (temp_fahrenheit - 32.0)/9.0)
print(f'{temp_celsius}° Celsius.')

# 8:
temp_kelvin = int(input("Escreva a temperatura em kelvin: "))
temp_celsius = round(temp_kelvin - 273.15, 2)
print(f'A temperatura é aproximadamente {temp_celsius}° Celsius.')

# 9:
temp_celsius = float(input("Escreva a temperatura em kelvin: "))
temp_kelvin = int(round(temp_celsius + 273.15))
print(f'A temperatura é aproximadamente {temp_kelvin}° Celsius.')

# 10:
veloc_km = int(input("Escreva a velocidade: "))
veloc_m = int(veloc_km/3.6)
print(f"{veloc_m} m/s.")

# 11:
veloc_m = int(input("Escreva a velocidade: "))
veloc_km = int(veloc_m * 3.6)
print(f"{veloc_km} km/h.")

# 12:
dist_milhas = int(input("Escreva a distância: "))
dist_km = int(round(1.61 * dist_milhas))
print(f"A distância é aproximadamente {dist_km}km.")

# 13:
dist_km = int(input("Escreva a distância: "))
dist_milhas = int(round(dist_km/1.61))
print(f"A distância é aproximadamente {dist_milhas}milhas.")

# 14:
ang_graus = int(input("Escreva o ângulo: "))
radiano = float(ang_graus * 3.14/180)
print(f"{radiano} rad.")

# 15:
radiano = float(input("Escreva o radiano: "))
ang_graus = int(radiano * 180/3.14)
print(f"{ang_graus}°.")

# 16:
polegadas = float(input("Escreva a quantidade de polegadas: "))
pole_int = int(polegadas)
centimetros = float(round(polegadas * 2.54, 2))
print(f"{pole_int} polegadas são(ou é) aproximadamente: {centimetros}cm.")

# 17:
centimetros = float(input("Escreva quantos centímetros: "))
cent_int = int(centimetros)
polegadas = float(round(centimetros / 2.54, 2))
print(f"{cent_int} centímetros são(ou é) aproximadamente: {polegadas} polegadas.")

# 18:
metros_cub = int(input("Escreva o valor em metros cúbicos:"))
litros = 1000 * metros_cub
print(f"{litros} litros.")

# 19:
litros = int(input("Escreva quantos litros: "))
metros_cub = int(litros / 1000)
print(f"{metros_cub} metros cúbicos.")

# 20:
massa = float(input("Escreva o valor da massa: "))
libras = float(round(massa / 0.45 , 1))
print(f"{libras} libras.")

# 21:
libras = float(input("Escreva o valor em libras: "))
massa = float(round(0.45 * libras, 1))
print(f"{massa} quilogramas.")

# 22:
jardas = float(input("Escreva um comprimento em jardas: "))
metros = float(round(0.91 * jardas, 1))
print(f"{metros} metros.")

# 23:
metros = float(input("Escreva um comprimento em metros: "))
jardas = float(round(metros / 0.91, 1))
print(f"{jardas} jardas.")

# 24:
area_metros = float(input("Escreva a área: "))
acres = float(round(area_metros * 0.000247, 4))
print(f"{acres} acres.")

# 25:
acres = float(input("Escreva o valor de acres:" ))
area_metros = float(round(acres * 4048.58))
print(f"{area_metros} metros quadrados.")

# 26:
area_metros = int(input("Escreva a área: "))
hectares = float(round(area_metros * 0.0001, 4))
print(f"{hectares} hectares.")

# 27:
hectares = float(input("Escreva quantos hectares: "))
area_metros = int(round(hectares * 10000))
print(f"{area_metros} metros quadrados.")

# 28:
valor1 = int(input("Escreva o valor 1: "))
valor2 = int(input("Escreva o valor 2: "))
valor3 = int(input("Escreva o valor 3: "))
soma = (valor1 * valor1) + (valor2 * valor2) + (valor3 * valor3)
print(f"{soma} é a soma dos quadrados dos valores.")

# 29:
nota1 = int(input("Escreva a nota 1: "))
nota2 = int(input("Escreva a nota 2: "))
nota3 = int(input("Escreva a nota 3: "))
nota4 = int(input("Escreva a nota 4: "))
media_aritmetica = ((nota1 + nota2 + nota3 + nota4)/4)
print(f"{media_aritmetica} é a média aritmética.")

# 30:
dolar = float(input("Escreva quanto está a cotação do dólar atualmente: "))
real = float(input("Escreva o valor em real: "))
conversao = float(round(real / dolar, 2))
print(f"{conversao} dólares.")

# 31:
numero = int(input("Escreva um número: "))
antecessor = int(numero - 1)
sucessor = int(numero + 1)
print(f"O antecessor é {antecessor} e o sucessor é {sucessor}.")

# 32:
numero = int(input("Escreva um número: "))
sucessor_triplo = int((numero * 3) + 1)
antecessor_dobro = int((numero * 2) - 1)
soma = sucessor_triplo + antecessor_dobro
print(f"A soma é {soma}.")

# 33:
tamanho_lado = int(input("Escreva o lado do quadrado: "))
area = tamanho_lado * tamanho_lado
print(f"A área do quadrado é {area}.")

# 34:
raio = int(input("Escreva o raio: "))
area_circulo = float(3.14 * (raio * raio))
print(f"A área do círculo é {area_circulo} centímetros quadrados.")

# 35:
import math
a = int(input("Escreva o primeiro cateto: "))
b = int(input("Escreva o segundo cateto: "))
hipotenusa = int(math.sqrt(a ** 2 + b ** 2))
print(f"{hipotenusa}")

# 36:
altura = int(input("Escreva a altura: "))
raio = int(input("Escreva o raio: "))
volume = int(3.14 * (raio ** 2) * altura)
print(f"{volume}.")

# 37:
valor = int(input("Escreva o valor do produto: "))
desconto = 12 / 100 * valor
total = int(valor - desconto)
print(f"{total}.")

# 38:
salario = float(input("Escreva seu salário: "))
aumento = 25 / 100 * salario
bruto = round(salario + aumento)
print(f"O novo salário será de {bruto} reais.")

# 39:
quantia = 780000
primeiro_ganhador = int(46 / 100 * quantia)
segundo_ganhador = int(32 / 100 * quantia)
terceiro_ganhador = int(quantia - primeiro_ganhador - segundo_ganhador)
print(f"O primeiro ganhador receberá {primeiro_ganhador} reais.")
print(f"O segundo ganhador receberá {segundo_ganhador} reais.")
print(f"O rerceiro ganhador receberá {terceiro_ganhador} reais.")

# 40:
diaria = int(input("Quantos dias o encanador trabalhou? "))
dia = diaria * 30.00
imposto_renda = 8 / 100 * dia
quantia_liq = (dia - imposto_renda)
print(f"O total ficou em {quantia_liq} reais.")

# 41:
horas_trabalhadas = int(input("Quantas horas de trabalho por dia? "))
horas_trabalhadas_mes = horas_trabalhadas * 30
valor_hora = int(input("Qual o valor por hora trabalhada? "))
salario_liq = int(valor_hora * horas_trabalhadas_mes)
aumento = 10 / 100 * salario_liq
salario_final = int(salario_liq + aumento)
print(f"O salario sem aumento é de {salario_liq} reais.")
print(f"O salário com aumento é de {salario_final} reais.")

# 42:
salario_base = int(input("Salário: "))
gratificacao = 5 / 100 * salario_base
imposto = 7 / 100 * salario_base
salario_final = int(salario_base + gratificacao - imposto)
print(f"O salário ajustado será de {salario_final} reais.")

# 43:
valor_total = int(input("Qual foi o valor total? "))
desconto = 10 / 100 * valor_total
parcela = float(round(valor_total / 3, 2))
comissao_a_vista = float(5 / 100 * (valor_total - desconto))
comissao_parcela = 5 / 100 * valor_total
print(f"Valor com desconto: {valor_total - desconto}.\nValor da parcela: {parcela}.\n"
      f"Comissão à vista: {comissao_a_vista}.\nComissão parcelado: {comissao_parcela}.")

# 44:
altura_degrau = float(input("Escreva a altura do degrau em centimetros: "))
altura_desejada = float(input("Escreva a altura que deseja alcançar em metros: "))
conversao_altura = altura_desejada * 100 #Conversão para centimetros
calculo = round((conversao_altura / altura_degrau))
print(f"Você precisará subir: {calculo} degraus.")

# 45:
letra = str(input("Escreva uma letra: "))
maiuscula = letra.upper()
print(f"{maiuscula}")

# 46:
numero = input("Escreva um número inteiro de 3 dígitos: ")
print(f"{numero[::-1]}")

# 47:
numero = input("Escreva um número inteiro de 4 dígitos: ")
lista = str(numero)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# 48:
valor_segundos = int(input("Escreva um valor em segundos: "))
hora = valor_segundos // 3600
resto_hora = valor_segundos % 3600
minuto = resto_hora // 60
resto_minuto = resto_hora % 60
print(f"{hora} horas,{minuto} minutos e {resto_minuto} segundos.")

# 49:
valor_segundos = int(input("Escreva horario em segundos: "))
hora = valor_segundos // 3600
resto_hora = valor_segundos % 3600
minuto = resto_hora // 60
resto_minuto = resto_hora % 60
print(f"A experiência começou às: {hora} horas, {minuto} minutos e {resto_minuto} segundos.")

valor_segundos2 = int(input("Escreva a duração da experiência em segundos: "))
hora2 = valor_segundos2 // 3600
resto_hora2 = valor_segundos2 % 3600
minuto2 = resto_hora // 60
resto_minuto2 = resto_hora % 60

print(f"Toda a soma de horário com duração, resultou em: "
      f"{hora + hora2} horas, {minuto + minuto2} minutos e {resto_minuto + resto_minuto2} segundos.")

# 50:
ano_atual = 2022
idade = int(input("Qual a sua idade? "))
print(f"Seu ano de nascimento é {(ano_atual - idade) - 1}.")

# 51:
x = int(input("Escreva a coordenada x: "))
y = int(input("Escreva a coordenada y: "))

soma = float((x ** 2 + y ** 2) ** (1/2))
print(f"O resultado das coordenadas é: {soma}.")

# 52:
valor_premio = float(input("Qual o valor do prêmio? "))
apostador_x = int(input("Qual a quantia que o maior apostador investiu? "))
apostador_y = int(input("Qual a quantia que o segundo maior apostador investiu? "))
apostador_z = int(input("Qual a quantia que o menor apostador investiu? "))

x = 0.5 * valor_premio
y = 0.35 * valor_premio
z = 0.15 * valor_premio

print(f"Primeiro ganhador: {x} reais;\n"
      f"Segundo ganhador: {y} reais;\n"
      f"Terceiro ganhador: {z} reais.")

# 53:
preco = int(input("Qual o preço do metro de tela? "))
comprimento = int(input("Escreva o comprimento em centimetros: "))
largura = int(input("Escreva a largura em centimetros: "))
preco_centimentro = preco / 100
area = comprimento * largura
total = area * preco_centimentro
print(f"O preço da tela ficará em: {total} reais.")
"""
