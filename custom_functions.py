import anki_vector
from anki_vector.util import degrees

def custom_turn(robot):
    # Custom function to make Vector turn 180 degrees
    robot.behavior.turn_in_place(degrees(180))

def custom_say_hello(robot):
    # Custom function to make Vector say "Hello"
    robot.behavior.say_text("Hello!")