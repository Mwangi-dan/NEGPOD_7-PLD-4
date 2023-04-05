import mysql.connector
import time
import webbrowser


class TriviaGame:
    """class of functions that allow the users to intellact with the Wildlife Trivia Game"""


    def __init__(self):
        self.q_number = 0
        self.score = 0

        self.terrestrial_qns = ["What is the colour of a giraffe's tongue?",
                                "Which animal is the only animal that can't jump? ",
                                "A cat's urine doesn't glow under black light? True or False:",
                                "Which mammal has a cube-shaped poop? ",
                                "What mammal carries leprosy? ",
                                "Dogs are not colour-blind but they can't see one colour, What's that colour? ",
                                "Koalas sleep partially the whole day. How many hours do you think they sleep up to? ",
                                ]

        self.terrestrial_answs = ['purple', 'elephant', 'true',
                                  'wombat', 'armadillo', 'blue' or 'yellow', '20' or 'twenty']

        self.aquatic_qns = ["What animal has no blood and no brain? ",
                            "I am a shrimp. Where is my heart located? ",
                            "What is the slowest fish? ",
                            "Which animal sleeps with only half of its brain at a time? ",
                            "Which sea creature has blue blood? ",
                            "Platypuses swim with their eyes closed. True or False? ",
                            "What is the most venomous fish? ",
                            "Which sea creature lays the biggest egg in the world?",
                            "How many hearts does an octopus have? ",
                            ]

        self.aquatic_answs = ['jellyfish', 'head', 'seahorse',
                            'dolphin', 'horseshoe crab' , 'true', 'reef stonefish', 'whale shark', 'three' or '3']
        
        self.aerial_qns = ["Which bird's head has to be upside when it eats?",
                           "What's the sense of a kiwi bird?",
                           "My eyes are bigger than my brain, What's my name?",
                           "59 " + "%" + " of my ratio are female-female breeding, Name the bird?",
                           "Owls don't have eyeballs, they have __.",
                           ]
        
        self.aerial_answs = ['flamingo', 'see' or 'smell', 'ostrich', 'house sparrow', 'eye tubes']

    def get_score(self):
        return self.score

    def ask_question(self, category):
        """function that asks question to the user"""

        if category == 1:
            print("\n" + self.terrestrial_qns[self.q_number])

        elif category == 2:
            print("\n" + self.aquatic_qns[self.q_number])
        
        elif category == 3:
            print("\n" + self.aerial_qns[self.q_number])
        else:
            print("Please enter the right category")


    def check_answer(self, category):
        """the functions which verfies if the user answer is right"""
        
        if category == 1:
            if self.q_number < len(self.terrestrial_qns) -1:
                user_answer = input("Please enter your answer here: ")
                correct_answer = self.terrestrial_answs[self.q_number]
                time.sleep(0.3)

                if user_answer.lower() == correct_answer.lower():
                    self.score += 1
                    print("Congratulations, you got it right")
                else:
                    print("Oooops, this is not the right answer.")
                    print("The right answer is " + correct_answer)
                self.q_number += 1
            else:
                header()
                print("Congratulations, you successfully completed the quiz")
                print("You scored: ", self.score, end="\n")

        elif category == 2:
            if self.q_number < len(self.aquatic_qns) -1:
                user_answer = input("Please enter your answer here: ")
                correct_answer = self.aquatic_answs[self.q_number]
                time.sleep(0.3)

                if user_answer.lower() == correct_answer.lower():
                    self.score += 1
                    print("Congratulations, you got it right")
                else:
                    print("Oooops, this is not the right answer.")
                    print("The right answer is " + correct_answer)
                self.q_number += 1
            else:
                header()
                print("Congratulations, you successfully completed the quiz")
                print("You scored: ", self.score, end="\n")

        elif category == 3:
            if self.q_number < len(self.aerial_qns) - 1:
                user_answer = input("Please enter your answer here: ")
                correct_answer = self.aerial_answs[self.q_number]
                time.sleep(0.3)

                if user_answer.lower() == correct_answer.lower():
                    self.score += 1
                    print("Congratulations, you got it right")
                else:
                    print("Oooops, this is not the right answer.")
                    print("The right answer is " + correct_answer)
                self.q_number += 1
            else:
                header()
                print("Congratulations, you successfully completed the quiz")
                print("You scored: ", self.score, end="\n")



            
def header():
    """
    simple header made up of asterisks
    """
    print("\n\t********************\n")


def game_play():
    """the functions that initialize the game"""
    
    header()
    print("Hello, Below is a menu of Wildlife categories: ")

    print("1. Terrestrial wildlife")
    print("2. Aquatic wildlife")
    print("3. Aerial wildlife\n")

    user_option = int(input("Please enter a number of the choice wildlife category to continue: "))
    game_one = TriviaGame()
    

    if user_option == 1:
        for i in range(7):
            game_one.ask_question(user_option)
            game_one.check_answer(user_option)
    elif user_option == 2:
        for i in range(9):
            game_one.ask_question(user_option)
            game_one.check_answer(user_option)
    else:
        for i in range(5):
            game_one.ask_question(user_option)
            game_one.check_answer(user_option)


    
    x = repeat()
    if x == 1:
        game_play()
    else:
        print("\nHope you learnt a lot and had fun.\nGoodbye!")
        
    return x


def db_connect():
    """
    Initializes daabase server credentialss
    """

    conn = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        passwd = "root",
        database = "users_db"
    )
    return conn


def verify_user(name):
    """
    verifies if user is in the database
    
    """

    conn = db_connect()
    
    cursor = conn.cursor()

    sql2 = "SELECT name FROM users"
    cursor.execute(sql2)
    rows = cursor.fetchall()

    for row in rows:
        if name in row:
            return True
    return False

    conn.close()

def register_user(name, pwd):
    """
    Registers a new user
    """
    conn = db_connect()
    
    cursor = conn.cursor()

    sql = "INSERT INTO users (name, password) VALUES (%s, %s)"
    data = (name, pwd)

    cursor.execute(sql, data)
    conn.commit()
    conn.close()

def get_score(name):
    """
    Gets the score of a user from the database
    """
    conn = db_connect()
    
    cursor = conn.cursor()
    sql2 = "SELECT name, score FROM users"
    cursor.execute(sql2)
    rows = cursor.fetchall()
    data = {}

    for a, b in rows:
        data.setdefault(a, []).append(b)

    for keys, values in data.items():
        if name in keys:
            print(values[0])


def save_score(name, user_score):
    """
    Saves score to database
    """
    conn = db_connect()

    cursor = conn.cursor()
    sql2 = "UPDATE `users_db`.`users` SET `score` = '%s' WHERE (`name` = '%s')"
    data = (user_score, name)
    cursor.execute(sql2, data)
    conn.commit()
    conn.close()

def replay(num):
    choice = int(input("\nDo you want to:\n 1. Play again\n2. Exit\nYour choice: "))
    if choice == 1:
        num = 1
        return num
    else:
        num = 5
        return num

def repeat():
    opt = int((input("\n1. Play again\n2. Exit\nYour choice: ")))
    return opt