foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you'd like to buy: (press q to quit): ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter the price of {food}: $"))
        prices.append(price)

print("_____ Food Cart _____")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total price: {total}$")