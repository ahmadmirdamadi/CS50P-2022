import random


def main():
    level = get_level()
    s = simulate_game(level)
    print(f"nomreh:{s}")


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1,2,3]:
                break
        except:
            pass
    return level



def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)

    else:
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x,y


def simulate_round(x,y):
    ct = 1
    while ct <=3:
        try:
            soal = int(input(f"{x} + {y} = "))
            if soal == (x+y):
                return True
            else:
                ct += 1
                print("EEE")
        except:
            ct += 1
            print("EEE")

    print(f"{x} + {y} = {x+y}")
    return False


def simulate_game(level):
    cr = 1
    s = 0
    while cr <= 10:
        x,y = generate_integer(level)
        res = simulate_round(x,y)
        if res == True:
            s += 1
        cr += 1
    return s


if __name__ == "__main__":
    main()