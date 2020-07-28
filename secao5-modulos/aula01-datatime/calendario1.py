from calendar import monthrange

dia_semana, ultimo_dia = monthrange(2020, 2)
# Retorna uma tupla contendo o número do dia na semana (0-6)
# e último dia de fevereiro de 2020
print(monthrange(2020, 2))
print(ultimo_dia)  # Saída: 29 (último dia de fevereiro de 2020)

# Saída - (5, 29)
# O 5 significa que é um sábado
# O 29 significa que este é o último dia do mês