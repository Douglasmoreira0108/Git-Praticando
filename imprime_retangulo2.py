l = int(input("Digite a largura: "))
h = int(input("Digite a altura: "))
c = "#"

def retângulo(l, h, c):
    linha_cheia = c * l
    if l > 2:
        linha_vazia = c + (" " * (l - 2)) + c
    else:
        linha_vazia = linha_cheia
    if h >= 1:
        print(linha_cheia)
    for i in range(h - 2):
        print(linha_vazia)
    if h >= 2:
        print(linha_cheia)
retângulo(l, h, c)
