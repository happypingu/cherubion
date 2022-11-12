from .data import DATA
from .get_input import get_input
from .generate_readable_list import generate_readable_list
from .built_in_methods import print_

def get_command(commands, list_options=False):
    while True:
        if list_options == True:
            print_(
                "You may enter: " + generate_readable_list(commands)
            )

        received_input = get_input()

        print_()

        if received_input in commands:
            return received_input

        print_(
            DATA["unsuitable_input_messages"]["get_command"].format(
                commands=generate_readable_list(commands)
            )
        )
