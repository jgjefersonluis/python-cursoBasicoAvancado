file = open('abc2.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendo linhas: ')
print(file.read())

file.close()