with open('abclendo.txt', 'a+') as file:
    file.write('Outra linha\n')
    file.seek(0)
    print(file.read())

