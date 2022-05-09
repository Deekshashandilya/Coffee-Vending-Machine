MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }}

resources = {
    "water": [300, "ml"],
    "milk": [200, "ml"],
    "coffee": [100, "g"],
}

money = [0, "$"]


# Display the initial prompt : type of coffee and report


def comparison():
    global resources
    temp = resources
    for item in MENU[choose]['ingredients']:
        if MENU[choose]['ingredients'][item] > resources[item][0]:
            print("Sorry there is not sufficient", item)
            # return resources,False
            return False
            break
            # print(resources[item])
            # print("All items are in enough quantity",item)
        else:
            temp[item][0] = resources[item][0] - MENU[choose]['ingredients'][item]
    resources = temp
    cost()
    print(f"Here is your {choose} .Enjoy !!.")
    # return temp,True
    # return


def cost():
    print("Please insert coins.")
    quarters = int(input("how many quarters? : "))
    dimes = int(input("how many dimes? : "))
    nickles = int(input("how many nickles? : "))
    pennies = int(input("how many pennies? : "))

    cal = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if cal >= MENU[choose]['cost']:
        balance = round(cal - MENU[choose]['cost'], 2)
        print(f"Here is ${balance} in change.")

        money[0] += MENU[choose]['cost']
        # return True
    else:
        print("Print Insufficent Money")
        # return False


def check_req(choose):
    if choose == 'report':
        for i in resources:
            print(f"{i} : {resources[i][0]}{resources[i][1]}")
        print("Money :", money[1], money[0])
    elif choose == 'latte':
        # print("latte")
        comparison()
        # print("Out of break")
        # cost()

    elif choose == 'espresso':
        # print("espresso")
        comparison()
    elif choose == 'cappuccino':
        # print("cappuccino")
        # if(comparison()):
        #   cost()
        comparison()
    elif choose == 'off':
        global set_flag
        set_flag = False
        print("Exit")
    else:
        print("You have made a Spell Error")


set_flag = True

while set_flag:
    choose = input("What would you like ? (Latte / Espresso / Cappuccino) : ").lower()
    check_req(choose)

# def money_cal(quarters,dimes,nickles,pennies,choose):
#   cal =quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
#   if cal >= MENU[choose]['cost']:
#     print(cal - MENU[choose]['cost'])
#   else:
#     print("Print Insufficent Money")


# money_cal(quarters,dimes,nickles,pennies,choose)


# #if report selected it will tell the balance of resources in machine
# #Select the type
# # insert the coins
# #ask for quartes , dimes ,nickels ,pennies ,
# #calculate the total amount inserted and show the balance
# #display the msg prompt for good coffee
# #repeat the program
