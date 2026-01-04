# shopping cart module
foods = []
prices = [] 
total = 0

while True:
    food = input("Enter food item (or 'q' to finish): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter price for {food}: "))
        foods.append(food)
        prices.append(price)
        total += price
        print(f"Added {food} for ${price:.2f}. Current total: ${total:.2f}")