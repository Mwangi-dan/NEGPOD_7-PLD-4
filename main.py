from classes_functions import *
from getpass import getpass

sign = True
print("\t*** Welcome to Wildlife Trivia ***")
print("Utilize this platform to learn more about wildlife\n")

MAX_TRIES = 3
run = True
user_sign_in = int(input("1. Login\n2. Sign up\n3. Play as guest\n4. Learn more\n5. Exit\nYour choice: "))

while run and MAX_TRIES > 0:

    if user_sign_in == 1:
        tries_left = 3
        log = False
        while tries_left > 0:
            while log == False:
                print("\nEnter your user name and password")
                user_name = input("User Name: ")
                user_pwd = getpass("Password: ")

                if verify_user(user_name) == True:
                    log = True
                    header()
                    print("Successfully logged in! Welcome", user_name)
                    x = game_play()
                    if x == 2:
                        run == False
                else:
                    print("Wrong username or password. Try again!\n")

            else:
                tries_left -= 1
                if tries_left > 0:
                    print(f"Invalid credentials. You have {tries_left} tries left.")
                else:
                    print("You have no tries left. Please try again later.")
                    run = False
                    break
    elif user_sign_in == 2:

        while sign == True:
            new_username = input("Enter username: ")
            new_user_pwd = input("Enter password: ")
            
            if verify_user(new_username) == True:
                print(new_username + " already in use. Try again!\n")
            else:
                sign = False
                register_user(new_username, new_user_pwd)
                x = game_play()
                if x == 2:
                    run = False
    
    elif user_sign_in == 3:
        x = game_play()
        if x == 2:
            run = False
    
    elif user_sign_in == 4:
        webbrowser.open_new("https://sowc.alueducation.com/")
        run = False
    
    else:
        print("Goodbye!")
        run = False