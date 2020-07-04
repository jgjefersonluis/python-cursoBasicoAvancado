string = '0123456789012345678901234567890123456789012345678901234567890123456789'
n=10
lista = [string[i:i + n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)





"""
print(string[0:10])
print(string[10:20])
print(string[20:30])
print(string[30:40])
print(string[50:60])
print(string[60:70])
"""
#####################################
"""
comp = [letra for letra in string]
print(comp)
"""