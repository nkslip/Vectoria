"""
vectoria — custom brain for anki vector.

cli for testing actions. connect to vector via wire-pod and run
registered actions by name.

usage:
    python main.py list              # show all actions
    python main.py run wave          # run an action
    python main.py run happy_dance   # run another
"""
import asyncio
import sys

import anki_vector

from actions import registry

# import to register all built-in actions
import example_actions  # noqa: F401


def list_actions():
    """Print all registered actions."""
    actions = registry.list()
    if not actions:
        print("no actions registered.")
        return
    print(f"\n  vectoria — {len(actions)} actions available\n")
    for action in sorted(actions, key=lambda a: a.name):
        tags = f"  [{', '.join(action.tags)}]" if action.tags else ""
        print(f"  {action.name:<20} {action.description}{tags}")
    print()


async def run_action(name: str):
    """Connect to vector and run an action by name."""
    action = registry.get(name)
    if not action:
        print(f"unknown action: {name}")
        print("use 'python main.py list' to see available actions")
        return

    print(f"connecting to vector...")
    with anki_vector.Robot() as robot:
        print(f"running: {action.name} — {action.description}")
        await registry.run(name, robot)
        print("done!")


def main():
    if len(sys.argv) < 2:
        print("usage: python main.py [list|run <action>]")
        return

    command = sys.argv[1]

    if command == "list":
        list_actions()
    elif command == "run":
        if len(sys.argv) < 3:
            print("usage: python main.py run <action_name>")
            return
        asyncio.run(run_action(sys.argv[2]))
    else:
        print(f"unknown command: {command}")
        print("usage: python main.py [list|run <action>]")


if __name__ == "__main__":
    main()
