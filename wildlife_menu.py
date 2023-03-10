# Welcoming user ot the game

print("Hello, Below is a menu of Wildlife categories : ")

# Function containing choices

def choices_menu():
    print("1. Terrestrial wildlife")
    print("2. Aquatic wildlife")
    print("3. Aerial wildlife\n")

choices_menu()

# Allowing user to input their choice

option = input("Please enter a number for your choice wildlife category to continue : ")


def learn_or_test(option_name):
    print("1. Learn more about ", option_name)
    print("2. Test your skills about ", option_name)

# IF Conditions getting option name associated with the user choice

if option=="1":
    learn_or_test("terrestrial wildlife")

elif option =="2":
    learn_or_test("aquatic wildlife")

else:
    learn_or_test("aerial wildlife")

# using webbrowser library to access links for learning and testing skills about wildlife

import webbrowser

second_option = input("Please enter a number for your choice to continue : ")

if second_option=="1":
    webbrowser.open_new("https://www.wildlifetrusts.org/learning")

else:
    webbrowser.open_new("https://lp.panda.org/wildlife-day-quiz")

