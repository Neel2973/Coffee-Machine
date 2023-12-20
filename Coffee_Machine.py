import coffee_menu
import Coffee_resources

MENU = coffee_menu.MENU
resources = Coffee_resources.resources


def money():
    quaters = float(input("How many quaters? "))
    dimes = float(input("How many dimes? "))
    nickel = float(input ("How many nickels? "))
    pennies = float(input("How many pennies? "))
    global given_money
    given_money = (0.25*quaters)+(0.1*dimes)+(0.05*nickel)+(0.01*pennies)
    for coffee,information in MENU.items():
        if coffee == choice and information['cost'] <= given_money:
            remaining_money = given_money - information['cost']
            remaining_money = round(remaining_money,2)
            print(f"Here's your change: {remaining_money}.")
            break
        elif information['cost'] > given_money:
            print("Sorry, that's not enough money. Money refunded.")
            break


def coffee(drink_name,order_ingredients):
    for items in resources:
        resources[items] -= order_ingredients[items]
    print(f"Here's your drink {drink_name}. Enjoy!")


def is_sufficient(drink_name,order_ingredients):
    for items in resources:
        if resources[items] < order_ingredients[items]:
            return f"Sorry there's no enough {items}."

is_on = True

while is_on:
    choice = input("What would you like to have? (espresso, latte, cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml,\nMilk: {resources['milk']}ml,\nCoffee: {resources['coffee']}g")
    else:
        drink = MENU[choice]
        result = is_sufficient(choice, drink['ingredients'])
        bool_value = bool(result)
        if bool_value == True:
            print(result)
            break

        else:
            money()
            if drink['cost'] <= given_money:
                coffee(choice,drink['ingredients'])






