from . import interface
from .battle.battle_util import PlayerHasDiedError
from .create_player import create_player
from .rooms.village import room as village
from .util import GameOver


def start_game():
    player = create_player()

    try:
        village.enter(player)
    except (PlayerHasDiedError, GameOver) as exception:
        if isinstance(exception, PlayerHasDiedError):
            interface.print_multiple_lines(
                lines=[
                    "=" * 20,
                    "",
                    "",
                    "",
                    "You have died",
                    "",
                    "",
                    "",
                    "=" * 20
                ],
                # TODO: CHANGE THIS TO 1 BACK
                delay=0
            )
        else:
            interface.sleep(7)
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
                    "..."
                ],
                delay=0
            )

            interface.print_()
            interface.sleep(7)
