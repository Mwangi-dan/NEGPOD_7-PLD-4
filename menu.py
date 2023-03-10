# Welcoming user ot the game

print("Hello, Below is a menu of Wildlife categories: ")

# Function containing choices

def choices_menu():
    print("1. Terrestrial wildlife")
    print("2. Aquatic wildlife")
    print("3. Aerial wildlife\n")

choices_menu()

# Allowing user to input their choice

option = input("Please enter a number of the choice wildlife category to continue :")


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

second_option = input("Please enter a number of the choice to continue :")

if second_option=="1":
    webbrowser.open_new("https://www.wildlifetrusts.org/learning")

else:
    score = 0

    if option == '3':
        q1 = input(f"Question 1: Which bird's head has to be upside when it eats?\n a. Flammingo\n b. Angel\n c. Bubba\n d. Baldy\n")

        if q1 =='a' or 'A':
            print(f"Congratulations!")
            score+=1
        else:
            print(f"incorrect choice!")

        q2 = input(f"Question 2: What's the sense of a kiwi bird?\n a. Smell\n c. See\n d. Touch\n e. Both a and c\n")
        if q2 =='e' or 'E':
            print(f"Congratulations!")
            score+=1
        else:
            print("incorrect choice!")

        q3 = input("Question 3: My eyes are bigger than my brain, What's my name?\n a. Angel\n b. Ostrich\n c. Flammingo\n d. Bird\n")

        if q3 =='':
            print("\nCongratulations!\n")
            score+=1
        else:
            print("\nincorrect choice!\n")

        q4 = input(f"Question 4: 59 " + "%" + " of my ratio are female-female breeding, Name the bird?\n a. House sparrow\n b. Duck\n c. Bird d. Bat\n")

        if q4 =='':
            print("Congratulations!")
            score+=1
        else:
            print("incorrect choice!")

        q5 = input("Question 5: Owls don't have eyeballs, they have ______.\n a. Eye tubes\n b. eye balls c. eye lenses\n d. eye lashes\n")

        if q5 =='a' or 'A':
            print("Congratulations!")
            score+=1
        else:
            print("incorrect choice!")
    print("your total score is :", str(score), " out of 5.")

    