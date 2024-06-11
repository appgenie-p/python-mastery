# Начальный объем данных
initial_volume_gb = 600

# Ежегодный прирост (10%)
annual_growth_rate = 0.10

# Количество лет
years = 5

# Расчет конечного объема данных через 5 лет
final_volume_gb = initial_volume_gb * (1 + annual_growth_rate) ** years
print(final_volume_gb)
