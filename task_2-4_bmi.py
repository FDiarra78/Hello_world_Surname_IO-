weight = 75
height_cm = 180

height_m = height_cm / 100

bmi = weight / (height_m ** 2)

print("Введите ваш вес (кг):", weight)
print("Введите ваш рост (см):", height_cm)
print("\n--- Отчет о состоянии здоровья ---")
print(f"Рост:\t{height_cm:.1f} см")
print(f"Вес:\t{weight:.1f} кг")
print(f"Индекс массы тела:\t{bmi:.2f}")