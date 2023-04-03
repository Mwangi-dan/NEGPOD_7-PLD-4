class TriviaGame:

    def __init__(self, choice=1):
        self.q_number = 0
        self.score = 0
        self.choice = choice

        self.terrestrial_qns = {1: "What is the colour of a giraffe's tongue?",
                                2: "Which animal is the only animal that can't jump? ",
                                3: "A cat's urine doesn't glow under black light? True or False:",
                                4: "Which mammal has a cube-shaped poop? ",
                                5: "What mammal carries leprosy? ",
                                6: "Dogs are not colour-blind but they can't see one colour, What's that colour? ",
                                7: "Koalas sleep partially the whole day. How many hours do you think they sleep up to? ",
                                }

        self.terrestrial_answs = {1: 'Purple', 2: 'Elephant', 3: 'True',
                                  4: 'Wombat', 5: 'armadillos', 6: 'blue' or 'yellow', 7: '20'}

        self.aquatic_qns = {1: "What animal has no blood and no brain? ",
                            2: "I am a shrimp. Where is my heart located? ",
                            3: "What is the slowest fish? ",
                            4: "Which animal sleeps with only half of its brain at a time? ",
                            5: "Which sea creature has blue blood? ",
                            6: "Platypuses swim with their eyes closed. True or False? ",
                            7: "What is the most venomous fish? ",
                            8: "Which sea creature lays the biggest egg in the world?",
                            9: "How many hearts does an octopus have? ",
                            }

        self.aquatic_answs = {1: 'The jellyfish', 2: 'On your head' or 'On the head', 3: 'The dwarf seahorse' or 'The seahorse',
                              4: 'The dolphin', 5: 'The horseshoe crab', 6: 'True', 7: 'The reef stonefish', 8: 'The whale shark', 9: 'Three'}

    def ask_question(self):
        if self.choice == '1':
            for items in self.terrestrial_qns.items():
                print(items[1])

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Congratulations, you got it right")


print("Hello, Below is a menu of Wildlife categories: ")

print("1. Terrestrial wildlife")
print("2. Aquatic wildlife")
print("3. Aerial wildlife\n")

# super.__init__("TriviaGame")
user_option = input(
    "Please enter a number of the choice wildlife category to continue :")

game_one = TriviaGame(choice=user_option)
game_one.ask_question()
