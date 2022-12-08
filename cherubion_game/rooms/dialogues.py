from .. import interface

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
    interface.print_multiple_lines(
        lines=[
            "- Tell me about Farun's jar, - you say to the priest, who has a look of resentment in his eyes.",
            "And fear. ",
            "Yes, you're sure that at the mention of the jar the priest shudders with fear.",
            "- There's nothing special about that jar... - he begins, then corrects himself quickly.",
            "- Apart, that is, from the fact that it is the last known handiwork of our Order's saint, the Great Farun, and is therefore held in extremely high esteem in our Church.",
            "You nod your head in agreement, but you remain curious, but you are sure that the priest will not spill the beans about the jar.",
            "Perhaps the innkeeper will...",
            "",
            "If you have finished speaking, say 'finished'",
            "If you'd like to ask about the area, say 'area'",
            "If you'd like to ask about Halumbar, say 'halumbar'."
        ],
        delay=0
    )