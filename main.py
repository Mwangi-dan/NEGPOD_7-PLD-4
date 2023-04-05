from classes_functions import *

if __name__ == "__main__":
    print("\t*** Welcome to Wildlife Trivia ***")
    print("Take this opportunity to learn more about our precious wildlife.\n")
    run = True
    user_sign_in = int(input("1. Login\n2. Sign up\n3. Play as guest\n4. Learn more\n5. Exit\nYour choice: "))
    while run == True:

        if user_sign_in == 1:
            user_name = input("User Name: ")
            user_pwd = input("Password: ")
        
            if verify_user(user_name) == True:
                print("\n\t********************\n")
                print("Successfully logged in! Welcome ", user_name)
                game_play()

            else:
                print("Invalid credentials")

        elif user_sign_in == 2:
            new_username = input("Enter username: ")
            new_user_pwd = input("Enter password: ")
            register_user(new_username, new_user_pwd)
            print("Successfully signed up! Welcome ", new_username)
            print("\t********************\n")
            game_play()
            replay()
            user_sign_in = replay()

        elif user_sign_in == 3:
            game_play()
        
        elif user_sign_in == 4:
            webbrowser.open_new("https://www.wildlifetrusts.org/learning")

        else:
            print("Goodbye!")
            run = False

