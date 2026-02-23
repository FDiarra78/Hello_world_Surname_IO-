reagent_name = "Sulfuric acid"
quantity = 5

report = f"Reagent {reagent_name} has been received in quantity {quantity} pcs."

print(report)

with open("inventory.txt", "w", encoding="utf-8") as f:
    f.write(report + "\n")

print("Report saved to inventory.txt")