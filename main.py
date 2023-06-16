import re

from generate import *

COMMANDS = {
    "add": lambda *args: add_words(*args),
    "exclude": lambda *args: exclude(*args),
    "exit": lambda *_: exit(),
    "include": lambda *args: include(*args),
    "regenerate": lambda *args: generate(args[0]),
    "remove": lambda *args: remove_words(*args),
    "reset": lambda *args: reset(args[0]),
}


def run():
    state: dict[str, set[str]] = {
        "inputs": get_inputs(),
        "include": set(),
        "exclude": set(),
    }

    generate(state)

    while True:
        command = input(": ")
        command, *args = re.sub(r"\s+", " ", command.strip()).split(" ")

        if command in COMMANDS:
            COMMANDS[command](state, *args)


def add_words(_state: dict[str, set[str]], *_args: str):
    _state["inputs"].update(_args)

    write_inputs(_state["inputs"])
    generate(_state)


def remove_words(_state: dict[str, set[str]], *_args: str):
    _state["inputs"].difference_update(_args)

    write_inputs(_state["inputs"])
    generate(_state)


def reset(_state: dict[str, set[str]]):
    _state["inputs"].clear()
    _state["include"].clear()

    write_inputs()
    write_outputs()


def include(_state: dict[str, set[str]], *_args: str):
    if len(_args) and _args[0] == "*":
        _state["include"].clear()
    else:
        _state["include"].update(_args)

    generate(_state)


def exclude(_state: dict[str, set[str]], *_args: str):
    if len(_args) and _args[0] == "*":
        _state["exclude"].clear()
    else:
        _state["exclude"].update(_args)

    generate(_state)


def write_inputs(_inputs: set[str] = set()):
    with open(INPUT_FILE_NAME, "w") as inputs_file:
        inputs_file.writelines([f"{word}\n" for word in sorted(_inputs)])


if __name__ == "__main__":
    run()
