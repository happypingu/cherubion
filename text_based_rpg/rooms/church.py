from .. import interface
from ..room import Room
from .village import continue_journey
from .village import enter_village

def first_church_dialogue():
    interface.print_multiple_lines(
        lines=[
            "A tiny church suits a tiny village.",
            "The building, whose roof is topped with a broken sword indicating that it is consecrated to some god, can accommodate only forty to fifty people at a time.",
            "In the cool foyer stands a tiny bier into which believers can drop their meager offerings.",
            "Inside the church, dozens of heavy wooden benches lie empty and rotting; everything looks poor.",
            "You don't have to look around long, one of the side doors opens and a grim-looking but very authoritative-looking man hurries towards you.",
            "- I am Father Fabricius! How can I help you, my son? - he asks inquiringly, as he quickly assesses what you might be like.",
            "After you've introduced yourself properly, the father leads you to a back room, which you suddenly can't decide whether it's a storeroom, a rest room or something else.",
            "- I need information, Father. - you say duly, leaning back in your chair. ",
            "- Ask your questions!",
            "",
            "If you'd like to ask a religious question, say 'religion'.",
            "If you'd like to ask the priest about the area, say 'area'"
        ],
        delay=0
    )

def religious_questions():
    interface.print_multiple_lines(
        lines=[
            "- Tell me about your faith! - you say to the priest.",
            "- I'm interested in everything...",
            "The priest nods in satisfaction, and starts a long, long story, which he continues for a good three hours.",
            "You listen carefully, because sometimes even the smallest piece of information can mean survival.",
            "The most important things you've learned:",
            "Breeze Hut, as this village is called, is the last stop before the Unclimbable Mountains and the Endless Wasteland.",
            "The latter is guarded by a gigantic black giant who not only makes you pay a toll, but also asks you three very strange questions.",
            "Before the wilderness lies the Forest of Twilight, and if you are brave enough, you can embark on extraordinary adventures.",
            "Deep in the forest lives a wizard who may know the answer to the giant's third question.",
            "Who knows the answer to the first two questions? - you lean closer to the priest.",
            "- I know the answer to the first one, - the holy man replies.",
            "- But I can only tell you if you bring me the Jar of Farun from the inn, which that scoundrel Halumbar keeps in his chest.",
            "",
            "If you'd like to ask about Halumbar, say 'halumbar'.",
            "If you'd like to ask about the Jar of Farun, say 'jar'.",
            "If you'd like to ask about the area, say 'area'."
        ],
        delay=0
    )

def halumbar_questions():
    interface.print_multiple_lines(
        lines=[
            "- Who is this Halumbar? - you ask the priest.",
            "- A two-faced scoundrel - replies the holy man -, who has recently stolen from me, by a vile trick, the sacred jar of our order, which was burnt from silver by the great Farun... ",
            "Since then all misfortune has fallen on my head, my followers have fallen away.",
            "",
            "If you have finished speaking, say 'finished'",
            "If you'd like to ask about the Jar of Farun, say 'jar'",
            "If you'd like to ask about the area, say 'area'"
        ],
        delay=0
    )

def area_questions():
    interface.print_multiple_lines(
        lines=[
            "- Tell me about the area! - you ask the priest.",
            "The priest nods and gives you a brief description of the most important things:",
            "The name of the village is Breeze Hut, and it is the last stop before the Unclimbable Mountains and the Endless Wasteland.",
            "No one has ever crossed the former, and the latter is guarded by a gigantic black giant.",
            "Before the wasteland lies the Forest of Twilight, where a cursed sorcerer is said to live.",
            "",
            "If you'd like to ask a religious question, say 'religion'.",
            "If you have finished speaking, say 'finished'"
        ],
        delay=0
    )

def finished_talking():
    interface.print_multiple_lines(
        lines=[
            "Finishing the conversation, you thank him for his help and head for the door.",
            "On the way, you glance briefly at the box where donations are being collected.",
            "",
            "If you'd like make a donation, say 'donate'.",
            "If you go on without making a donation, say 'continue'."
        ],
        delay=0
    )

def make_a_donation():
    interface.print_multiple_lines(
        lines=[
            "You stand by the bushel and reach into your money bag.",
            "Your fingers feel the heavy coins, and the question of how much to give runs through your mind.",
            "",
            "If you want to give less than a gold, say 'less'",
            "If you want to give between 1 and 5 gold, say 'few'",
            "If you want to give more than 5 gold, say 'lot'"
        ],
        delay=0
    )

def continue_your_way():
    interface.print_multiple_lines(
        lines=[
            "You stop for just a moment by the bushel.",
            "You do not fail to notice the priest hiding in the shadows, watching your actions, but you have no intention of giving. ",
            "Not now.",
            "The street is quiet, you see no passersby, and there is no life behind the fences. ",
            "It seems as if everyone is on their midday rest.",
            "Where to now?",
            "",
            "If you'd like to head towards the inn, say 'inn'",
            "If you'd like to go to the shop, say 'shop'.",
            "If you'd like to leave the village, say 'leave'."
        ],
        delay=0
    )

def leave_village():
    interface.print_multiple_lines(
        lines=[
            "Soon you will leave the village behind. ",
            "You walk on without a word, and after a short while you notice a forest shrouded in mist to the east. ",
            "You find this extremely strange, as the sky is clear and the sun is shining brightly. ",
            "You can find no reasonable explanation for the fog, unless... ",
            "Unless it's magic.",
            "",
            "If you want to go closer to inspect the forest shrouded in mist, say 'forest'.",
            "If you want to continue your journey, say 'continue'."
        ],
        delay=0
    )

def jar_questions():
    print('asd')

# Page 229
def enter(room, player):
    first_church_dialogue()

    additional_commands = ["religion", "area"]
    command = interface.get_game_command(player, room, additional_commands)
    while True:
        if command == "religion": # Page 49
            religious_questions()

            additional_commands.clear()
            additional_commands = ["halumbar", "jar", "area"]
            command = interface.get_game_command(player, room, additional_commands)

            if command == "halumbar": # Page 303
                halumbar_questions()

                additional_commands.clear()
                additional_commands = ["finished", "jar", "area"]
                command = interface.get_game_command(player, room, additional_commands)

                if command == "finished":
                    finished_talking()

                    additional_commands.clear()
                    additional_commands = ["donate", "continue"]
                    command = interface.get_game_command(player, room, additional_commands)

                    if command == "donate": # page 20
                        make_a_donation()

                        additional_commands.clear()
                        additional_commands = ["less", "few", "lot"]
                        command = interface.get_game_command(player, room, additional_commands)

                        # TODO: MONEY SYSTEM
                    
                    if command == "continue": # page 286, 159
                        continue_your_way()

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
                            leave_village()

                            additional_commands.clear()
                            additional_commands = ["forest", "continue"]
                            command = interface.get_game_command(player, room, additional_commands)

                            if command == "forest":
                                from .forest import room as forest
                                forest.enter(player)

                            if command == "continue":
                                continue_journey()

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
                                    enter_village()

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

                if command == "jar":
                    jar_questions()

                if command == "area":
                    pass

            if command == "jar": # Page 23
                print('u said jar')

            if command == "area": # Page 312
                pass

        if command == "area": # Page 318
            area_questions()

            additional_commands.clear()
            additional_commands = ["religion", "finished"]
            command = interface.get_game_command(player, room, additional_commands)

room = Room(
    enter=enter
)