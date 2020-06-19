"""
Iterando strings com while em python
"""
while True:
    minha_string = input('Digite uma frase')
    tamanho_string = len(minha_string)

    c = 0
    contagem_atual = 0
    letra = ''
    while c < tamanho_string:
        qtd_vezes_letras = minha_string.count(minha_string[c])

        if contagem_atual < qtd_vezes_letras and minha_string[c].strip():
           letra = minha_string[c]
           contagem_atual = qtd_vezes_letras

        c += 1
    print(letra, contagem_atual)

'''
nova_string = ''
while c < tamanho_string:

    if minha_string[c] == 'r':
        nova_string = nova_string + minha_string[c].upper()

    else:
        nova_string = nova_string + minha_string[c]

  #  print(nova_string)
    c += 1
    print(nova_string)
'''
