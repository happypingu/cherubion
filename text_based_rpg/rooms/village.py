from .. import interface
from ..room import Room

def first_dialogue():
    interface.print_multiple_lines(
        lines=[
                "Dark clouds floated over the gloomy rocky crags of Ars-Umthar.",
                "Lightning tore the sky to shreds, and the dull roar of thunder shook the earth.",
                "On the cliff-top, a great fortress defied the wrath of the gods.",
                "Its towering walls braved the fierce blasts of tornado-force winds, even the all-encompassing thunderbolts of lightning.",
                "Behind the walls, in the basement of one of the towers, nine determined nobles gathered to put an end once and for all to the evil practices of the sorcerer Fluvar Thorgas, which was beginning to threaten all of Cherubion.",
                "After many years of hard work and sacrifice of life and money, they have gathered the three magical items that will finally send Sorcerer Thorgas back to the place where he emerged from one dark and nasty night:",
                "the darkness of the Underworld.",
                "On a low ivory table before the noblemen lay the Eye of Terror, the most hideous and murderous statue ever created in the world of Cherubion.",
                "Beside it lay the crystal prism of the sorcerer Chorax, showing the past, present and future to those who knew how.",
                "The third object was the scimitar of Atura, the heroic barbarian prince, the only weapon on Cherubion's western shores capable of cutting the golden thread of a non-mundane being, binding him to Cherubion with its evil magic.",
                "The noble lords looked at each other, their faces grim from the trials they had endured, but their eyes now glittered with the triumphant spark of perceived victory. ",
                "The first nobleman raised his hand and began the ceremony.",
                "At that moment, a bolt of lightning, stronger than ever, split the sky in two, splitting the tower in two, and the nine noblemen were in the depths of it.",
                "The force of the lightning scattered the tower's huge boulders, tore apart the magical shields protecting the basement, and destroyed the nobles gathered for the ceremony.",
                "Dust and ash flew in the air, and from somewhere in the distance, the wind carried an eerie laughter.",
                "...",
                "...",
                "...",
                "You arrive in this land as a lonely traveller.",
                "I have always been attracted by unknown landscapes and foreign people.",
                "Of course, it's no mean feat if you manage to acquire a good supply of gold coins to buy everything you need.",
                "There is only one thing you value more than shiny, shiny gold coins: knowledge.",
                "You're interested in magic, but you're also keen to spend time deciphering long-forgotten inscriptions that might lead you on a new adventure.",
                "Emerging from behind a small grove, you see a friendly-looking settlement.",
                "Then two dozen houses, a small church, a single street.",
                "It's not much, but it's a place to refresh your supplies and gather information about the countryside.",
                "",
                "If you'd like to enter the village, say 'enter'.",
                "If you'd like to continue your journey avoiding the village, say 'avoid'."
        ],
        delay=0
    )


def enter_village():
    # Page 89
    interface.print_multiple_lines(
                lines = [
                    "You soon cut through the only street in the village.",
                    "Your face looks impassive, but you are not distracted.",
                    "You see children lurking between the bars of the fence, peaceful villagers working peacefully, seemingly oblivious to you, but you can almost feel their eyes on you.",
                    "When you leave the village, you turn around and start walking back with determination.",
                    "You have seen three buildings that may need your attention: the church, a small shop and the inn called \"Silver Antlers\".",
                    "Of course, you could stop to talk to the villagers, but you know from experience how distrustful they are of strangers.",
                    "On the other hand, anyone who hopes to get money from you, be it a shopkeeper or even a sacristan, is more likely to talk.",
                    "",
                    "If you'd like to enter the church, say 'church'",
                    "If you'd like to head towards the shop, say 'shop'",
                    "If you'd like to visit the inn, say 'inn'"
                ],
                delay=0
            )


def avoid_village():
    # Page 274
    interface.print_multiple_lines(
                lines=[
                    "Although the village seems friendly, for now you feel there's no point spending your money, as the forest provides fresh game meat and there's still a clear stream in your way.",
                    "As for information, perhaps it's better to discover everything yourself rather than listen to superstitious villagers' tales.",
                    "You have had enough experience with such folk.",
                    "You'll take the trouble to go around the village in a wide arc.",
                    "Making sure no one has seen you, you continue on your way in complete peace.",
                    "Soon you spot a forest shrouded in mist to the east.", 
                    "This is extremely strange, as the sky is clear and the sun is shining brightly. ",
                    "You can find no reasonable explanation for the mist unless...",
                    "Unless it is magic.",
                    "",
                    "If you want to go closer to inspect the forest shrouded in mist, say 'forest'.",
                    "If you don't want to go on an adventure just yet, and would rather continue on your way, say 'continue'."
                ],
                delay=0
            )


def continue_journey():
    # Page 348
    interface.print_multiple_lines(
                lines=[
                    "Even the forest in the mist cannot ignite the fire of adventure in your soul.",
                    "You avert your eyes from the strange phenomenon and continue on your way. ",
                    "Soon you leave the forest behind you, and after a few hours' walk you see a vast plain spreading out to the east, while to the north, where your journey continues, you are blocked by towering mountains.",
                    "To the west, a dark line stretches across the land, and even from here you can tell that a wide cleft of rock has torn up the land, making the road impassable.",
                    "",
                    "If you continue your journey towards the mountains, say 'mountains'.",
                    "If you'd like to head towards the plains, say 'plains'.",
                    "If you'd like to return to the village, say 'village'.",
                    "If you'd like to inspect the forest, say 'forest'.",
                ],
                delay=0
            )

def enter(room, player):
    first_dialogue()

    additional_commands = ["enter", "avoid"]
    command = interface.get_game_command(player, room, additional_commands)

    while True:
        if command == "enter":
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
        
        if command == "avoid":
            avoid_village()

            additional_commands.clear()
            additional_commands = ["forest", "continue"]
            command = interface.get_game_command(player, room, additional_commands)

            if command == "forest": # Page 165
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


room = Room(
    enter=enter
)