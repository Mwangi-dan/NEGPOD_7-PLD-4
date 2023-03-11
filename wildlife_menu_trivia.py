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
    # Terrestrial questions
    score = 0

    if option == '1':
        print("TRIVIA QUESTIONS")

        q1 = input("What is the colour of a giraffe's tongue? ") 
        if q1 == 'purple':
            print("Congratulations!\n")
            score += 1
        else:
            print("Incorrect choice\n")

        q2 = input("Which animal is the only animal that can’t jump? ")
        if q2 == 'Elephant':
            print("Congratulations!\n")
            score += 1
        else:
            print("Incorrect choice\n")

        # ask team about this one
        q3 = input("A cat’s urine doesn’t glow under black light? True or False: ")
        if q2 == 'True':
            print("Congratulations!\n")
            score += 1
        else:
            print("Incorrect choice\n")

        q4 = input("Which mammal has a cube-shaped poop? ")
        if q4 == 'Wombat':
            print("Congratulations!\n")
            score += 1
        else:
            print("Incorrect choice\n")

        q5 = input("What mammal carries leprosy? ")
        if q5 == 'armadillos':
            print("Congratulations!\n")
            score += 1
        else:
            print("Incorrect choice\n")

        q6 = input("Dogs are not colour-blind but they can’t see one colour, What’s that colour? ")
        if q6 == 'blue' or 'yellow':
            print("Congratulations!\n")
            score += 1
        else:
            print("Incorrect choice\n")

        q7 = input("Koalas sleep partially the whole day. How many hours do you think they sleep up to? ")
        if q7 == '20':
            print("Congratulations!\n")
            score += 1
        else:
            print("Incorrect choice\n")

        print("Well done on completing the trivia.\nYour total score is:\b {:d}".format(score))
