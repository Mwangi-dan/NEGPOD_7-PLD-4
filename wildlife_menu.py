# Welcoming user of the game
# Function containing choices
def choices_menu():
    print("Hello, Below is a menu of Wildlife categories:")
    print("1. Terrestrial wildlife")
    print("2. Aquatic wildlife")
    print("3. Aerial wildlife\n")

# Allowing user to input their choice
def learn_or_test(option_name):
    print("1. Learn more about ", option_name)
    print("2. Test your skills about ", option_name)


if __name__ == "__main__":
    choices_menu()
    user_choice = input("Which category do you want to learn about?")

    learn_or_test(user_choice)

