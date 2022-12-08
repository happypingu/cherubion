from .. import interface
from ..room import Room
from . import dialogues

# Page 229
def enter(room, player):
    dialogues.first_church_dialogue()

    additional_commands = ["religion", "area"]
    command = interface.get_game_command(player, room, additional_commands)
    while True:
        if command == "religion": # Page 49
            dialogues.religious_questions()

            additional_commands.clear()
            additional_commands = ["halumbar", "jar", "area"]
            command = interface.get_game_command(player, room, additional_commands)

            if command == "halumbar": # Page 303
                dialogues.halumbar_questions()

                additional_commands.clear()
                additional_commands = ["finished", "jar", "area"]
                command = interface.get_game_command(player, room, additional_commands)

                if command == "finished":
                    pass

                if command == "jar": # Page 23
                    pass

                if command == "area":
                    pass

            if command == "jar": # Page 23
                dialogues.jar_questions()

                additional_commands.clear()
                additional_commands = ["finished", "area", "halumbar"]
                command = interface.get_game_command(player, room, additional_commands)

                if command == "finished":
                    pass

                if command == "area":
                    pass

                if command == "halumbar":
                    pass

            if command == "area": # Page 312
                pass
            
            if command == "finished":
                pass

        if command == "area": # Page 318
            dialogues.area_questions()

            additional_commands.clear()
            additional_commands = ["religion", "finished"]
            command = interface.get_game_command(player, room, additional_commands)

            if command == "religion":
                pass

            if command == "finished":
                pass
        
        if command == "finished":
            dialogues.finished_talking()

            additional_commands.clear()
            additional_commands = ["donate", "continue"]
            command = interface.get_game_command(player, room, additional_commands)

            if command == "donate": # page 20
                dialogues.make_a_donation()

                additional_commands.clear()
                additional_commands = ["less", "few", "lot"]
                command = interface.get_game_command(player, room, additional_commands)

                # TODO: MONEY SYSTEM
            
            if command == "continue": # page 286, 159
                dialogues.continue_your_way()

                additional_commands.clear()
                additional_commands = ["inn", "shop", "leave"]
                command = interface.get_game_command(player, room, additional_commands)

                if command == "shop": # Page 23
                    from .shop import room as shop
                    shop.enter(player)

                if command == "inn": # Page 312
                    from .inn import room as inn
                    inn.enter(player)
                    
                if command == "leave": # Page 196
                    dialogues.leave_village()

                    additional_commands.clear()
                    additional_commands = ["forest", "continue"]
                    command = interface.get_game_command(player, room, additional_commands)

                    if command == "forest":
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