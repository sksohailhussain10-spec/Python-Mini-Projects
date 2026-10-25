import random
import sys


class RPS:
    def __init__(self):

        print('welcome to The Game Of Rock,Paper and Scissors ✨')
        print(''' 
                 • Rock     beats   Scissors 
                 • Scissors beatS   Paper 
                 • Paper    beats   Rock   
                 • If dont want  to play then Enter -> exit''')

        self.moves: dict = {'rock': '🧱 - Rock', 'paper': '🧾- Paper', 'scissors': '✂ - Scissors'}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):

        user_move: str = input('choose -> rock,paper,or scissors?>> ').lower()

        if user_move == 'exit':
            print('You have exited the game!')
            sys.exit()

        if user_move not in self.valid_moves:
            print('invalid movies....')
            return self.play_game()

        comp_move: str = random.choice(self.valid_moves)
        self.display_moves(user_move, comp_move)
        self.check_move(user_move, comp_move)

    def display_moves(self, user_move: str, comp_move: str):
        print('-------')
        print(f'Your choice      : {self.moves[user_move]}')
        print(f"computer's choice: {self.moves[comp_move]}")
        print('-------')

    def check_move(self, user_move: str, comp_move: str):
        if user_move == comp_move:
            print('Result -> Match is a tie!')
        elif user_move == 'rock' and comp_move == 'scissors':
            print('Result -> you have won the game')
        elif user_move == 'scissors' and comp_move == 'paper':
            print('Result -> congratulation you win!')
        elif user_move == 'paper' and comp_move == 'rock':
            print('Result -> you win!!!')
        else:
            print('Computer wins Wins....🎭better luck next time')
        play_again = input("play again?(yes/no): ").lower()
        if play_again == 'yes':
            rps.play_game()
        elif play_again == 'no':
            print('Thank you for playing😊')
            sys.exit()
        else:
            print('Invalid input...Please try again')


if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()