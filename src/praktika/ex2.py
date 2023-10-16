import random

def main():
    cube = random.randint(1, 6)
    print(f"{cube=}")
    if cube in (5, 6):
        print("you win")

    elif cube in (3, 4):
        main()


if __name__ == "__main__":
    main()