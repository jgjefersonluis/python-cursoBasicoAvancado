list = [12, 14, 15, 16, 19 ,20]
x=int(input(list))
def busca_binaria(lista, x):
    primeiro = 0
    ultimo= len(list)-1

    while primeiro<= ultimo:
        meio=(primeiro + ultimo)//2
        if lista[meio] ==x:
            return meio
        else:
            if x < lista[meio]:
                ultimo = meio -1
            else:
                primeiro = meio + 1
    return -1
print(busca_binaria(list, x))