import anki_vector
from custom_functions import custom_turn, custom_say_hello

def main():
    with anki_vector.Robot() as robot:
        custom_turn(robot)
        custom_say_hello(robot)

if __name__ == "__main__":
    main()