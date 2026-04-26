"""
vectoria built-in actions.

import this module to register all default actions with the registry.
each action is an async function that takes a robot instance and
orchestrates sdk calls to create a behavior.
"""
import asyncio

from anki_vector.util import degrees, speed_mmps

from actions import registry


@registry.register("wave", description="wave hello", tags=["greeting"])
async def wave(robot):
    robot.behavior.say_text("hi there!")
    robot.motors.set_lift_motor(5)
    await asyncio.sleep(0.3)
    robot.motors.set_lift_motor(-5)
    await asyncio.sleep(0.3)
    robot.motors.set_lift_motor(5)
    await asyncio.sleep(0.3)
    robot.motors.set_lift_motor(0)


@registry.register(
    "happy_dance", description="spin + green eyes + yay!", tags=["reaction"]
)
async def happy_dance(robot):
    robot.behavior.set_eye_color(0.25, 1.0)  # green
    robot.behavior.say_text("yay!")
    for _ in range(2):
        robot.behavior.turn_in_place(degrees(120))
        await asyncio.sleep(0.5)
    robot.behavior.set_eye_color(0.58, 1.0)  # back to blue


@registry.register(
    "blender_spin",
    description="spin fast like a tiny blender",
    tags=["silly"],
)
async def blender_spin(robot):
    robot.behavior.set_eye_color(0.05, 1.0)  # orange
    robot.behavior.say_text("vrrrrrrrr!")
    for _ in range(4):
        robot.behavior.turn_in_place(degrees(360))
        await asyncio.sleep(0.3)
    robot.behavior.set_eye_color(0.58, 1.0)  # back to blue


@registry.register(
    "angry_stomp",
    description="slam lift arm + red eyes + growl",
    tags=["reaction"],
)
async def angry_stomp(robot):
    robot.behavior.set_eye_color(0.0, 1.0)  # red
    for _ in range(3):
        robot.motors.set_lift_motor(5)
        await asyncio.sleep(0.2)
        robot.motors.set_lift_motor(-5)
        await asyncio.sleep(0.2)
    robot.behavior.say_text("grrrr!")
    robot.motors.set_lift_motor(0)
    await asyncio.sleep(1)
    robot.behavior.set_eye_color(0.58, 1.0)


@registry.register(
    "shy_peek",
    description="slowly peek up, look around, hide",
    tags=["personality"],
)
async def shy_peek(robot):
    robot.behavior.set_eye_color(0.75, 0.5)  # soft purple
    robot.motors.set_head_motor(1)
    await asyncio.sleep(1)
    robot.behavior.turn_in_place(degrees(30))
    await asyncio.sleep(0.5)
    robot.behavior.turn_in_place(degrees(-60))
    await asyncio.sleep(0.5)
    robot.behavior.say_text("oh!")
    robot.motors.set_head_motor(-3)
    await asyncio.sleep(0.5)
    robot.motors.set_head_motor(0)
    robot.behavior.set_eye_color(0.58, 1.0)


@registry.register(
    "celebrate",
    description="full celebration — spin + flash eyes + cheer",
    tags=["reaction", "stream"],
)
async def celebrate(robot):
    robot.behavior.say_text("woohoo!")
    colors = [0.0, 0.15, 0.35, 0.55, 0.75, 0.95]  # rainbow hues
    for hue in colors:
        robot.behavior.set_eye_color(hue, 1.0)
        robot.behavior.turn_in_place(degrees(60))
        await asyncio.sleep(0.2)
    robot.behavior.set_eye_color(0.58, 1.0)


@registry.register(
    "sad", description="lower head + blue eyes + whimper", tags=["reaction"]
)
async def sad(robot):
    robot.behavior.set_eye_color(0.58, 1.0)  # blue
    robot.motors.set_head_motor(-3)
    await asyncio.sleep(1)
    robot.behavior.say_text("aww...")
    robot.motors.set_head_motor(0)
