import random


class RockPaperScissors:
    """
    Main class for the Rock, Paper, Scissors game
    """
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def get_user_choice(self):
        """Method to get Users choice.      

        :return: User's choice as a sring.
        """
        user_choice = input(f"Enter your choice between: {self.choices}")
        if user_choice.lower() in self.choices:
            return user_choice
        else:
            print(f"Invalid input. Enter a choice among {self.choices}")
            return self.get_user_choice()
      
    def get_computer_choice(self):
        """Method to get a random choice from computer.

        :return: computer's choice as a string.
        """
        computer_choice = random.choice(self.choices)
        return computer_choice
    
    def decide_winner(self, user_choice, computer_choice):
        """Method to decide game winner based on the rules.

        :param user_choice: The user's choice
        :type user_choice: str
        :param computer_choice: The computer's choice
        :type computer_choice: str
        :return: Game winner
        """
        if user_choice == computer_choice:
            return "Tie!"
        win_combinations = [
            ('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')
            ]
        for win_comb in win_combinations:
            if user_choice == win_comb[0] and computer_choice == win_comb[1]:
                return "You won!"
        else:
            return "Computer won!"
     
    def play(self):
        """Main method to play Rock, Paper, Scissors game.
        """
        computer_choice = self.get_computer_choice()
        user_choice = self.get_user_choice()
        print(f"user's choice: {user_choice}, computer's choice: {computer_choice}")
        print(self.decide_winner(user_choice, computer_choice))


if __name__ == '__main__':
    game = RockPaperScissors()
    while True:
        game.play()
        continue_game = input("Do you want to play again? press any key for continue or (q/Q) for exit.")
        if continue_game.lower() == "q":
            break   