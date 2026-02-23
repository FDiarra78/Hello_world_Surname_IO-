name = "Фатумата Диарра"
date = "17.02.2026"
experiment = "Исследование памяти мышей"
conclusion = """В ходе эксперимента выявлены нарушения
долговременной памяти у экспериментальной
группы животных."""

print("+---+---+")
print("| Электронный лабораторный журнал    |    |")
print("+---+---+")
print(f"| ФИО исследователя : {name}    |    |")
print(f"| Дата    : {date}    |    |")
print(f"| Эксперимент    : {experiment}    |    |")
print("+---+---+")
print()
print("Вывод:")
print(conclusion)

with open("journal.txt", "w", encoding="utf-8") as f:
    f.write("+---+---+\n")
    f.write("| Электронный лабораторный журнал    |    |\n")
    f.write("+---+---+\n")
    f.write(f"| ФИО исследователя : {name}    |    |\n")
    f.write(f"| Дата    : {date}    |    |\n")
    f.write(f"| Эксперимент    : {experiment}    |    |\n")
    f.write("+---+---+\n")
    f.write("\nВывод:\n")
    f.write(conclusion + "\n")

print("\n✅ Файл journal.txt создан!")
