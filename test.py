import random

def main_program():
    x = random.randint(1, 10)
    playerInput = input()

    if(input == x):
        print("you win, the number was", x)
    else:
        print("you lose, the number was", x)
if __name__ == '__main__':
        main_program()