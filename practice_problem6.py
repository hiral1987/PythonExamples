import random


class Player:
    def __init__(self):
        self.guess_count = 0
        self.guessed_num = -1

    def increase_count(self):
        self.guess_count += 1


if __name__ == '__main__':
    a = int(input('Enter first number\n'))
    b = int(input('Enter second number\n'))

    print(f'You have generated first number: {a} & second number: {b}\n')

    randomNum = random.randint(a, b)
    # print(f'Number generated :{randomNum}\n')

    player1 = Player()
    player2 = Player()

    print(f'Now player1 will guess number')

    while player1.guessed_num != randomNum:
        player1.guess_count += 1
        player1.guessed_num = int(input('Please guess no\n'))

    print(f'player1 guess in {player1.guess_count} attempts\n')

    randomNum = random.randint(a, b)

    print(f'Now player2 will guess number\n')

    while player2.guessed_num != randomNum:
        player2.guess_count += 1
        player2.guessed_num = int(input('Please guess no\n'))

    print(f'player2 guess in {player2.guess_count} attempts\n')

    if player1.guess_count > player2.guess_count:
        print(f'player2 wins')
    elif player1.guess_count < player2.guess_count:
        print(f'player1 wins')
    else:
        print(f'Both player guess in same attempts')