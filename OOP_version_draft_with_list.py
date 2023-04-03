class TriviaGame:

    def __init__(self, choice=1):
        self.q_number = 0
        self.score = 0
        self.choice = choice

        self.terrestrial_qns = ["What is the colour of a giraffe's tongue?",
                                "Which animal is the only animal that can't jump? ",
                                "A cat's urine doesn't glow under black light? True or False:",
                                "Which mammal has a cube-shaped poop? ",
                                "What mammal carries leprosy? ",
                                "Dogs are not colour-blind but they can't see one colour, What's that colour? ",
                                "Koalas sleep partially the whole day. How many hours do you think they sleep up to? ",
                                ]

        self.terrestrial_answs = ['Purple', 'Elephant', 'True',
                                  'Wombat', 'armadillos', 'blue' or 'yellow', '20']

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

        self.aquatic_answs = {1: 'The jellyfish', 2: 'On your head' or 'On the head', 3: 'The dwarf seahorse' or 'The seahorse',
                              4: 'The dolphin', 5: 'The horseshoe crab', 6: 'True', 7: 'The reef stonefish', 8: 'The whale shark', 9: 'Three'}

    def ask_question(self):
        temp = self.terrestrial_qns[self.q_number]
        print(str(temp))
        self.q_number += 1
        # break

    def check_answer(self):
        if self.q_number < len(self.terrestrial_qns):
            user_answer = input("Please enter your answer here : ")
            correct_answer = self.terrestrial_answs[self.q_number]

            if user_answer.lower() == correct_answer.lower():
                self.score += 1
                print("Congratulations, you got it right")
            else:
                print("Oooops, this is not the right answer.")
            
        else:
            print("Congratulations, you sccuessfully completed the quiz")





print("Hello, Below is a menu of Wildlife categories: ")

print("1. Terrestrial wildlife")
print("2. Aquatic wildlife")
print("3. Aerial wildlife\n")

user_option = input(
    "Please enter a number of the choice wildlife category to continue :")

game_one = TriviaGame()

for i in range(7):

    game_one.ask_question()
    # break
    game_one.check_answer()
