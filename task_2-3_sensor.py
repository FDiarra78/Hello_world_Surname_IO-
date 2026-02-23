operator_name = "Фатумата Д"
pressure_value = 101.3

print("=== ЛОГ ДАТЧИКА ===")
print("Введите имя оператора:", operator_name)
print("Введите текущее значение давления (Па):", pressure_value, "Па")
print()

with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write(f"ОПЕРАТОР\tЗНАЧЕНИЕ\n")
    file.write(f"{operator_name}\t{pressure_value} Па\n")

print("✅ Данные успешно сохранены в 'sensor_log.txt'.")