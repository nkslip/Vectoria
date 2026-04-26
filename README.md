# vectoria

custom brain and personality layer for anki vector.

uses [wire-pod](https://github.com/kercre123/wire-pod) as the server
and [wirepod-vector-sdk](https://pypi.org/project/wirepod-vector-sdk/)
to control vector programmatically.

docs live in [cortex/vectoria/](https://github.com/nkslip/cortex/tree/main/vectoria).

---

## setup

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

requires wire-pod running and vector connected to it.

## usage

```
python main.py list              # show all actions
python main.py run wave          # wave hello
python main.py run happy_dance   # spin + green eyes + yay!
python main.py run blender_spin  # spin fast like a tiny blender
python main.py run celebrate     # rainbow eyes + spin + cheer
```

## adding actions

create a new file or add to `example_actions.py`:

```python
from actions import registry

@registry.register("my_action", description="does a thing", tags=["custom"])
async def my_action(robot):
    robot.behavior.say_text("doing a thing!")
    robot.behavior.turn_in_place(degrees(360))
```

import it in `main.py` and it's automatically available.

## available actions

- `wave` — wave hello
- `happy_dance` — spin + green eyes + yay!
- `blender_spin` — spin fast like a tiny blender
- `angry_stomp` — slam lift arm + red eyes + growl
- `shy_peek` — slowly peek up, look around, hide
- `celebrate` — rainbow eyes + spin + cheer
- `sad` — lower head + blue eyes + whimper
