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
        if q2 == '':
            print("Congratulations!\n")
            score += 1
        else:
            print("Incorrect choice\n")

        # ask team about this one
        q3 = input("A cat’s urine doesn’t glow under black light? True or False: ")
        if q2 == '':
            print("Congratulations!\n")
            score += 1
        else:
            print("Incorrect choice\n")

        q4 = input("Which mammal has a cube-shaped poop? ")
        if q4 == '':
            print("Congratulations!\n")
            score += 1
        else:
            print("Incorrect choice\n")

        q5 = input("What mammal can catch leprosy? ")
        if q5 == '':
            print("Congratulations!\n")
            score += 1
        else:
            print("Incorrect choice\n")

        q6 = input("Dogs are not colour-blind but they can’t see one colour, What’s that colour? ")
        if q6 == '':
            print("Congratulations!\n")
            score += 1
        else:
            print("Incorrect choice\n")

        q7 = input("Koalas sleep partially the whole day. How many hours do you think they sleep up to? ")
        if q7 == '':
            print("Congratulations!\n")
            score += 1
        else:
            print("Incorrect choice\n")

        print("Well done on completing the trivia.\nYour total score is:\b {:d}".format(score))

    # Aquatic Wildlife
    option = '2'
    user_answer = ' '
    score = 0

    if option == '2':
        print("TRIVIA QUESTIONS")

        q1 = input("What animal has no blood and no brain? ")
        if q1 == 'The jellyfish':
            print("Congratulations!")
            score += 1
        else:
            print("Incorrect choice.")

        q2 = input("I am a shrimp. Where is my heart located? ")
        if q2 == 'On your head':
            print("Congratulations!")
            score += 1
        if q2 == 'On the head':
            print("Congratulations!")
            score += 1
        if q2 == 'The head':
            print("Congratulations!")
            score += 1
        else:
            print("Incorrect choice.")

        q3 = input("What is the slowest fish? ")
        if q3 == 'The dwarf seahorse':
            print("Congratulations!")
            score += 1
        if q3 == 'The seahorse':
            print("Congratulations!")
            score += 1
        else:
            print("Incorrect choice.")
    
        q4 = input("Which animal sleeps with only half of its brain at a time? ")
        if q4 == 'The dolphin':
            print("Congratulations!")
            score += 1
        else:
            print("Incorrect choice.")
    
        q5 = input("Which sea creature has blue blood? ")
        if q4 == 'The horseshoe crab':
            print("Congratulations!")
            score += 1
        else:
            print("Incorrect choice.")
    
        q6 = input("Platypuses swim with their eyes closed. True or False? ")
        if q6 == 'True':
            print("Congratulations!")
            score += 1
        else:
            print("Incorrect choice.")

        q7 = input("What is the most venomous fish? ")
        if q7 == 'The reef stonefish':
            print("Congratulations!")
            score += 1
        else:
            print("Incorrect choice.")
    
        q8 = input("Which sea creature lays the biggest egg in the world?")
        if q8 == 'The whale shark':
            print("Congratulations!")
            score += 1
        else:
            print("Incorrect choice.")

        q9 = input("How many hearts does an octopus have? ")
        if q9 == 'Three':
            print("Congratulations!")
            score += 1
        else:
            print("Incorrect choice.")

        print("Well done on completing the trivia.\nYour total score is:\b {:d}".format(score))

