# 1:
x = 0
"""
nota = float(input("Escreva sua nota: "))
while nota > 10:
    print("Nota inválida")
    nota = float(input("Escreva novamente sua nota: "))
else:
    print("Nota válida!\nObrigado!")
    x = x + 1

# 2:
nome = input("Escreva seu nome de usuário: ")
senha = input("Escreva sua senha: ")
while senha == nome:
    print("Sua senha não pode ser igual ao nome de usuário.")
    senha = input("Reescreva uma senha, por favor: ")
else:
    print("Sua senha é válida, obrigado.")
    x = x + 1

# 3:
while x == 0:
    nome = input("Escreva um nome: ")
    idade = int(input("Escreva a idade: "))
    salario = float(input("Escreva o salário: "))
    sexo = input("Escreva o sexo (f ou m):")
    estado_civil = input("Escreva o seu estado civíl(s, c, v, d): ")

    while len(nome) <= 3:
        nome = input("Seu nome precisa ter mais de 3 caractéres: ")

    while (idade > 150) or (idade < 0):
        idade = int(input("Sua idade precisa estar entre 0 e 150 anos: "))

    while salario < 0:
        salario = int(input("Seu salário precisa estar positivo: "))

    while (sexo != "f") and (sexo != "m"):
        sexo = input("Seu sexo precisa ser ou 'f' ou 'm', se não, você é mutante: ")

    while (estado_civil != "s") and (estado_civil != "c") and (estado_civil != "v") and (estado_civil != "d"):
        estado_civil = input("Seu estado civíl deve ser s, c, v ou d: ")

    else:
        print("Informações válidas, obrigado.")
        x = x + 1
"""
# 4:
A = int(input("Escreva a ordem de habitantes do país 'A': "))
taxa_a = 3 / 100
B = int(input("Escreva a ordem de habitantes do país 'B': "))
taxa_b = 1.5 / 100

while A <= B:
    taxa1 = A * taxa_a
    taxa2 = B * taxa_b

print("O país 'A' alcançou o país 'B' em crescimento populacional.")


