volume = float(input("Введите нужный объем раствора (мл): "))

# 2. Расчёт массы соли
salt_mass = volume * 0.009

# 3. Объём воды
water_volume = volume

# 4. Affichage à l'écran
print("\n--- ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ ---")
print(f"Общий объем: {volume} мл")
print(f"Масса соли: {salt_mass:.2f} г")
print(f"Объем воды: {water_volume} мл")

# 5. Запись в файл
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("---\n")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли: {salt_mass:.2f} г\n")
    file.write(f"Объем воды: {water_volume} мл\n")

print("\n✅ Рецепт сохранён в файл recipe.txt")