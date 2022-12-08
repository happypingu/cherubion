from .. import interface
from ..room import Room
from . import dialogues

def enter(room, player):
    dialogues.first_dialogue()

    additional_commands = ["enter", "avoid"]
    command = interface.get_game_command(player, room, additional_commands)

    while True:
        if command == "enter":
            dialogues.enter_village()

            additional_commands.clear()
            additional_commands = ["church", "shop", "inn"]
            command = interface.get_game_command(player, room, additional_commands)

            if command == "church": # Page 229
                from .church import room as church
                church.enter(player)

            if command == "shop": # Page 23
                from .shop import room as shop
                shop.enter(player)

            if command == "inn": # Page 312
                from .inn import room as inn
                inn.enter(player)
        
        if command == "avoid":
            dialogues.avoid_village()

            additional_commands.clear()
            additional_commands = ["forest", "continue"]
            command = interface.get_game_command(player, room, additional_commands)

            if command == "forest": # Page 165
                from .forest import room as forest
                forest.enter(player)

            if command == "continue":
                dialogues.continue_journey()

                additional_commands.clear()
                additional_commands = ["mountains", "plains", "village", "forest"]
                command = interface.get_game_command(player, room, additional_commands)

                if command == "mountains":
                    from .mountain import room as mountain
                    mountain.enter(player)
                
                if command == "plains":
                    from .plains import room as plains
                    plains.enter(player)
                
                if command == "forest":
                    from .forest import room as forest
                    forest.enter(player)
                
                if command == "village":
                    dialogues.enter_village()

                    additional_commands.clear()
                    additional_commands = ["church", "shop", "inn"]
                    command = interface.get_game_command(player, room, additional_commands)

                    if command == "church": # Page 229
                        from .church import room as church
                        church.enter(player)

                    if command == "shop": # Page 23
                        from .shop import room as shop
                        shop.enter(player)

                    if command == "inn": # Page 312
                        from .inn import room as inn
                        inn.enter(player)


room = Room(
    enter=enter
)