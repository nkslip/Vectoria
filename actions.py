"""
vectoria action registry.

every custom behavior is an "action" — a named, reusable combo of
sdk calls (movement, speech, eye color, etc.) that can be triggered
by name from the cli, api, or stream events.

usage:
    from actions import registry

    # list all actions
    registry.list()

    # run an action
    await registry.run("happy_dance", robot)

    # register a new action
    @registry.register("my_action", description="does a thing")
    async def my_action(robot):
        robot.behavior.say_text("doing a thing!")
"""
import asyncio
import functools
from dataclasses import dataclass, field


@dataclass
class Action:
    """A registered action."""

    name: str
    description: str
    fn: callable
    tags: list[str] = field(default_factory=list)


class ActionRegistry:
    """Central registry for all vectoria actions."""

    def __init__(self):
        self._actions: dict[str, Action] = {}

    def register(
        self, name: str, description: str = "", tags: list[str] | None = None
    ):
        """Decorator to register an action function."""

        def decorator(fn):
            self._actions[name] = Action(
                name=name,
                description=description or fn.__doc__ or "",
                fn=fn,
                tags=tags or [],
            )

            @functools.wraps(fn)
            async def wrapper(*args, **kwargs):
                return await fn(*args, **kwargs)

            return wrapper

        return decorator

    def list(self) -> list[Action]:
        """Return all registered actions."""
        return list(self._actions.values())

    def get(self, name: str) -> Action | None:
        """Get an action by name."""
        return self._actions.get(name)

    async def run(self, name: str, robot, **kwargs) -> bool:
        """Run an action by name. Returns True if found and executed."""
        action = self._actions.get(name)
        if not action:
            return False
        await action.fn(robot, **kwargs)
        return True


# global registry — import this from anywhere
registry = ActionRegistry()
