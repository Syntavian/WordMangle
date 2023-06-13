import re

from generate import *

COMMANDS = {
    "add": lambda *args: add_words(*args),
    "exit": lambda *_: exit(),
    "regenerate": lambda *args: generate(args[0]),
    "remove": lambda *args: remove_words(*args),
    "reset": lambda *_: reset(),
}


def run():
    inputs = get_inputs()

    generate(inputs)

    while True:
        command = input(": ")
        command, *args = re.sub(r"\s+", " ", command.strip()).split(" ")

        if command in COMMANDS:
            COMMANDS[command](inputs, *args)


def add_words(_inputs: set[str], *_args):
    _inputs.update(_args)

    write_inputs(_inputs)
    generate(_inputs)


def remove_words(_inputs: set[str], *_args):
    _inputs.difference_update(_args)

    write_inputs(_inputs)
    generate(_inputs)


def reset():
    write_inputs()
    write_outputs()


def write_inputs(_inputs=[]):
    with open(INPUT_FILE_NAME, "w") as inputs_file:
        inputs_file.writelines([f"{word}\n" for word in sorted(_inputs)])


if __name__ == "__main__":
    run()
