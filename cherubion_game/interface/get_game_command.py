from .get_command import get_command
from .built_in_methods import print_
from ..player import races

_STATS = "stats"

_BASE_COMMANDS = [
    _STATS,
]

def get_game_command(player, room, additional_commands=[]):
    commands = additional_commands.copy()
    commands.extend(_BASE_COMMANDS)

    while True:
        print_()
        command = get_command(commands, True)

        if command in additional_commands:
            return command

        if command == _STATS:
            info = races.Hero(player.ourrace)
            print(info)