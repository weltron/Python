import random


def main():
    level = get_level()
    quiz = 1
    attempts = 3
    score = 0

    while quiz <= 10:
        x, y = generate_integer(level)
        round = attempt(x, y)
        if round == True:
            score += 1
        quiz += 1
    print("Score: ", score)


def attempt(x, y):
    tries = 3
    while tries > 0:
        try:
            guess = int(input(f"{x} + {y} = "))
            if guess != (x + y):
                print("EEE")
                tries -= 1
            else:
                return True
        except:
            tries -= 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False


def get_level():
    while True:
        try:
            level = int(input("Level:"))
            if level in [1, 2, 3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
