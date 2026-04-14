name = "Food Palace"
item1, price1 = "Pizza Peperoni", '7.20 Euro'
item2, price2 = "Burger Palace", '8.50 Euro'
item3, price3 = "Salad", '4.50 Euro'
item4, price4 = "Pasta", '3.25 Euro'


print("Welcome to", name, "\n")

print("=== MENU ===")

print(f"{item1}.......{price1}")
print(f"{item2}........{price2}")
print(f"{item3}................{price3}")
print(f"{item4}................{price4}")

"""

Цените са string
'7.20 Euro'

👉 Това работи, но не е „програмистко мислене“

💡 По-добре:
price1 = 7.20

и после:

print(f"{price1:.2f} Euro")

"""

"""
Подравняването (много важно!)

В момента:

.......   ........   ................

👉 не е подравнено добре

🔥 Професионален начин:
print(f"{item1:<20} {price1:.2f} Euro")

📌 <20 = подравнява текста вляво с ширина 20

"""

"""
name = "Food Palace"

item1, price1 = "Pizza Pepperoni", 7.20
item2, price2 = "Burger Palace", 8.50
item3, price3 = "Salad", 4.50
item4, price4 = "Pasta", 3.25

print(f"--- Welcome to {name} ---\n")

print("=== MENU ===\n")

print(f"{item1:<20} {price1:.2f} Euro")
print(f"{item2:<20} {price2:.2f} Euro")
print(f"{item3:<20} {price3:.2f} Euro")
print(f"{item4:<20} {price4:.2f} Euro")

"""

#OVERALL = 5.80