import random


class Rps:

    def __init__(self):
        self.rate = int()
        self.user_choice = str()
        self.chose = str()
        self.option_list = []
        self.dict_names = {}

        self.name = input("Enter your name:")

        self.default_options = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}
        self.default_choice = ['rock', 'paper', 'scissors']

        self.defeat = dict(
            water=['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'],
            dragon=['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
            devil=['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
            gun=['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
            rock=['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
            fire=['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
            scissors=['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
            snake=['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
            human=['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
            tree=['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
            wolf=['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
            sponge=['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
            paper=['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
            air=['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
            lightning=['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'])

        self.choices = ['rock', 'paper', 'scissors', 'fire', 'lightning',
                        'devil', 'dragon', 'snake', 'gun', 'tree',
                        'human', 'wolf', 'sponge', 'water', 'air']

        self.correct_words = ['rock', 'paper', 'scissors', 'fire', 'lightning', 'wolf',
                              'devil', 'dragon', 'snake', 'gun', 'tree', 'human', 'water',
                              'air', 'sponge', '!exit', '!rating']

    def data(self):
        print("Hello, " + self.name)
        with open('rating.txt') as search:
            for line in search:
                line = line.rstrip()
                yo = line.split()
                if self.name == yo[0]:
                    key, values = yo[0], int(yo[1].rstrip())
                    self.dict_names[key] = values
        self.option_list = input()
        print("Okay, let's start")
        self.user_input()

    def user_input(self):
        self.user_choice = str(input())
        self.chose = random.choice(self.default_choice if len(self.option_list) == 0 else self.choices)
        if self.user_choice not in self.correct_words:
            print("Invalid input")
            self.user_input()
        while self.user_choice != "!exit":
            if self.user_choice == "!rating" and self.name in self.dict_names:
                print("Your rating:", self.dict_names[self.name])
                self.user_input()
            self.decision()
            self.user_input()
        print("Bye!")
        exit()

    def decision(self):
        if self.user_choice == self.chose:
            self.dict_names[self.name] += 50
            print(f"There is a draw ({self.chose})")
        elif len(self.option_list) != 0 and self.chose not in self.defeat[self.user_choice]:
            print(f"Sorry, but the computer chose {self.chose}")
        elif len(self.option_list) == 0 and self.default_options[self.user_choice] == self.chose:
            print(f"Sorry, but the computer chose {self.chose}")
        else:
            self.dict_names[self.name] += 100
            print(f"Well done. The computer chose {self.chose} and failed")


rps = Rps()
rps.data()
